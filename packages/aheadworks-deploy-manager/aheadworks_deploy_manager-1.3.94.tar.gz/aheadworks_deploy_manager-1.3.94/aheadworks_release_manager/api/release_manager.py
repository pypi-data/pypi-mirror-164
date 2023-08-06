from aheadworks_core.api.jira_api_manager import JiraApiManager
from aheadworks_core.api.discord_api_manager import DiscordApiManager
from aheadworks_core.api.magento_manager import MagentoManager
from aheadworks_core.api.file_manager import FileManager
from aheadworks_core.model.parser.json import Json as JsonParser
from aheadworks_core.model.http.api_request import ApiRequest
from aheadworks_core.model.data.data_object import DataObject
from aheadworks_core.model.cd import Cd as cd
from datetime import datetime
from urllib.parse import urlparse
import os
import subprocess
import json
import shutil
import boto3


class ReleaseManager:
    """api manager for release"""

    RELEASE_PACK_TASK_LABEL = 'RELEASE-PACK'
    PD_TASK_LABEL = 'PD'
    TEST_TASK_LABEL = 'TEST'

    LICENCE = """/**
 * Aheadworks Inc.
 *
 * NOTICE OF LICENSE
 *
 * This source file is subject to the EULA
 * that is bundled with this package in the file LICENSE.txt.
 * It is also available through the world-wide-web at this URL:
 * https://aheadworks.com/end-user-license-agreement/
 *
 * @package    <PACKAGE_NAME>
 * @version    <VERSION>
 * @copyright  Copyright (c) <COPYRIGHT_YEAR> Aheadworks Inc. (https://aheadworks.com/)
 * @license    https://aheadworks.com/end-user-license-agreement/
 */\n"""

    def __init__(self, jira_api_config):
        self.jira_api_config = jira_api_config
        self.jira_api_manager = JiraApiManager(config=self.jira_api_config)
        self.discord_api_manager = DiscordApiManager()
        self.magento_manager = MagentoManager()
        self.file_manager = FileManager()
        self.json_parser = JsonParser()
        self.aws_s3 = boto3.resource('s3')

    def jira_release(self, jira_project_key, composer_file, discord_bot_url, path_to_files, assign_to):
        module_version = self.json_parser.get_variable_from_file('version', composer_file)
        # module_version = self.magento_manager.get_module_version(path_to_module)

        print('jira project key: ' + jira_project_key)
        print('module version: ' + module_version)
        print('discord bot url: ' + discord_bot_url)
        print('path to files: ' + path_to_files)
        print('assign to, account id: ' + assign_to)

        if not jira_project_key:
            print('jira_project_key is empty, skip jira release.')
            return False

        jira_instance = self.jira_api_manager.get_jira_instance()

        files_to_upload = []
        file_names = os.listdir(path_to_files)
        for file_name in file_names:
            files_to_upload.append(('file', (file_name, open(path_to_files + '/' + file_name, 'rb'))))

        jql = 'labels%3D{}-{}'.format(jira_project_key, module_version)
        links = self.get_release_tasks(jql)

        release_task_key = links[self.RELEASE_PACK_TASK_LABEL]['key']
        pd_task_key = links[self.PD_TASK_LABEL]['key']
        test_task_key = links[self.TEST_TASK_LABEL]['key']

        # add attachments
        self.add_attachments_to_task(release_task_key, files_to_upload)

        # module_dependencies = self.magento_manager.get_module_dependencies(path_to_module)
        module_dependencies = self.magento_manager.get_module_dependencies_from_composer(composer_file)
        composer_package_name = ','.join(list(map(lambda x: x['full_module_name'], module_dependencies.values())))

        # assign release pack to user
        release_issue = jira_instance.issue(release_task_key)
        release_issue.update(assignee={'accountId': assign_to})
        jira_instance.add_comment(release_issue, 'Composer Package Name:\n' + composer_package_name)

        # uncomment if needed check transitions for issue
        # transitions = jira_instance.transitions(release_issue)
        # set done to pd and test issue. transition=31 - Task Done
        pd_issue = jira_instance.issue(pd_task_key)
        jira_instance.transition_issue(pd_issue, transition=31)

        test_issue = jira_instance.issue(test_task_key)
        jira_instance.transition_issue(test_issue, transition=31)

        # release current version
        version = jira_instance.get_project_version_by_name(jira_project_key, module_version)
        release_date = datetime.today().strftime('%Y-%m-%d')
        version.update(released=True, releaseDate=release_date)

        project = jira_instance.project(jira_project_key)

        msg = '{} {}\n'.format(project.name, module_version)
        msg += '\n'.join(list(map(lambda x: x['url'], links.values())))
        msg += '\n' + self.jira_api_manager.get_release_report_all_issues_url(jira_project_key, version.id)

        self.discord_api_manager.send_msg(discord_bot_url, msg)

        return True

    def get_release_tasks(self, jql):
        links = dict()
        search_labels = [self.RELEASE_PACK_TASK_LABEL, self.PD_TASK_LABEL, self.TEST_TASK_LABEL]
        tasks = self.jira_api_manager.search_tasks_jql(jql)
        if 'issues' in tasks and len(tasks['issues']):
            for task in tasks['issues']:
                if 'labels' in task['fields'] and 'labels' in task['fields']:
                    task_labels = task['fields']['labels']
                    label_intersection = list(set(task_labels) & set(search_labels))
                    if len(label_intersection) == 1:
                        task_key = task['key']
                        task_url = self.jira_api_manager.get_issue_url(task_key)
                        links[label_intersection[0]] = dict({'url': task_url, 'key': task_key})
                    else:
                        raise Exception('Incorrect labels count found.')
                else:
                    raise Exception('Labels not found.')
        else:
            print(tasks)
            raise Exception('Release Tasks not found.')

        return links

    def add_attachments_to_task(self, task_key, files):
        tasks = self.jira_api_manager.add_attachments_to_task(task_key, files)

    def build_swagger_web_api_doc(
            self,
            path_to_module,
            magento_url,
            magento_path_on_server='/var/www/html',
            ssh_port=22,
            ssh_user='root',
            ssh_pass='root'
    ):
        obj = DataObject()
        obj.url = magento_url
        obj.auth_type = 'none'
        magento_request = ApiRequest(obj)

        aws_bucket_name = 'aheadworks_cdn'
        aws_swagger_web_api_doc_path = 'swagger_web_api_doc/'
        magento_app_code_path_on_server = magento_path_on_server + '/app/code'
        tmp_dir_m2_modules = '/var/tmp/m2_modules'

        parent_module_name = self.magento_manager.get_module_name(path_to_module)
        if not os.path.isfile(path_to_module + '/etc/webapi.xml'):
            return 'Skip Web API doc generation: file etc/webapi.xml has been not found for module {}'.format(
                parent_module_name)

        parsed_url = urlparse(magento_url)

        try:
            list_of_module_paths = self.magento_manager.download_modules_from_git(path_to_module, tmp_dir_m2_modules)
            self.magento_manager.upload_modules_to_server_by_ssh(
                list_of_module_paths['dir_app_code'],
                magento_app_code_path_on_server,
                parsed_url.hostname,
                ssh_port,
                ssh_user,
                ssh_pass
            )
            module_names = ','.join(list_of_module_paths['module_names'])
            magento_request_url = '/generate_web_api_json.php?module_names={}'.format(module_names)
            # workaround, for generate magento cache
            magento_request.get(location=magento_request_url)
            # here we generate json with cache from previous step
            swagger_json = magento_request.get(location=magento_request_url)

            try:
                json.loads(swagger_json)
            except Exception as error:
                print("Invalid respone from Swagger:\n{}\n\n".format(swagger_json))
                raise Exception(error)

            s3_result = self.aws_s3.Bucket(aws_bucket_name).put_object(
                Key=aws_swagger_web_api_doc_path + parent_module_name.lower() + '_latest.json',
                Body=swagger_json,
                ACL='public-read'
            )
            os.system('rm -rf ' + tmp_dir_m2_modules)
        except Exception as error:
            os.system('rm -rf ' + tmp_dir_m2_modules)
            raise Exception(error)

        result = 'Web Api Doc Path: https://media.aheadworks.com/{}\n'.format(s3_result.key)
        result += 'Magento Request Url: {}\n'.format(magento_request_url)
        return result

    def build_ecommerce_pack(self, bitbucket_workspace, bitbucket_repo_slug):
        request = 'api.bitbucket.org/2.0/repositories/{}/{}/downloads'.format(
            bitbucket_workspace,
            bitbucket_repo_slug
        )

        extraRepositories = os.environ.get('COMPOSER_REPOSITORIES', "")             #COMPOSER_REPOSITORIES--variable in module repo settings
        if extraRepositories != "":
            try:
                composer = json.loads(extraRepositories)
                for item in composer:
                    composer_install = 'composer config -g repositories.'
                    name = item['name']
                    tool_type = item['type']
                    url = item['url']
                    name_n_tool = name + ' ' + tool_type
                    os.system(composer_install + name_n_tool + ' ' + url)
            except:
                print('Json invalid, check, is your repositories data is correct')
        else:
            print('Empty composer_repositories variable')

        with open('./composer.json') as f:
            composer = json.load(f)
        license_template = self.LICENCE

        core_module_name = composer['name']
        module_dependencies = self.magento_manager.get_module_dependencies('./')
        tmp_dir = os.getcwd()
        os.system("cd /var/www/html && composer require " + core_module_name)
        os.system("cd" + ' ' + tmp_dir)

        # @todo use self.magento_manager.download_modules_from_git(path_to_module, tmp_dir_m2_modules)
        os.system('apk add zip')
        os.system("mkdir -p app/code/Aheadworks")
        os.system("mkdir /build_archives")
        with cd('app/code/Aheadworks'):
            for full_module_name, module_item in module_dependencies.items():
                if self.magento_manager.is_suggested_module(tmp_dir, full_module_name):
                    os.system("cd /var/www/html && composer require " + full_module_name)
                    os.system("cd" + ' ' + tmp_dir)
                module = module_item['module_name']
                shutil.copytree("/var/www/html/vendor/aheadworks/" + module, os.getcwd() + "/" + module)
                path_to_composer = module + "/composer.json"
                path_to_registration = module + "/registration.php"
                ec1 = os.path.isfile(path_to_composer)
                ec2 = os.path.isfile(path_to_registration)
                if not (ec1) or not (ec2):
                    raise Exception(module + " haven't build")

                self.file_manager.remove_files_and_dirs_ignore_case(
                    module,
                    ['bitbucket-pipelines.yml', 'readme.md', '.gitignore'],
                    ['.git']
                )
                # todo end
                # change to FileManager add_info_to_file_header
                self.add_license_to_php_files(os.getcwd() + '/' + module, license_template)
                os.system(
                    "echo See https://aheadworks.com/end-user-license-agreement/ >> " + module + "/license.txt")

                with open(path_to_registration) as f2:
                    lines = f2.readlines()
                for line in lines:
                    if line.find("headworks_") != -1:
                        module_directory_name = line.strip('\"\'').split('_')[1][0:-3]
                is_core = core_module_name.split('/')[1] == module
                if is_core:
                    marketplace_name = core_module_name.split('/')[1]
                    core_module_directory_name = module_directory_name
                    result_name = module_directory_name + '-' + composer['version']
                os.system('mv ' + module + ' ' + module_directory_name)
                if not is_core:
                    with open('./' + module_directory_name + '/composer.json') as f5:
                        meta_composer = json.load(f5)
                        module_zip_name = meta_composer['name'].split('/')[1]
                    self.make_archive('./' + module_directory_name + '/.', module_zip_name + '.zip')
                    os.system(
                        'curl -X POST "https://IgorSednev:FAdCM9dzPXzMYsbypdXe@' + request.strip() + '" ' + '--form files=@"' + module_zip_name + '.zip"')
                    os.system('cp ' + module_zip_name + '.zip /build_archives')
                    os.system('rm ' + module_zip_name + '.zip')
        with cd('app/code/Aheadworks/' + core_module_directory_name):
            os.system('zip -r ' + marketplace_name + '.zip ' + './')
            os.system(
                'curl -X POST "https://IgorSednev:FAdCM9dzPXzMYsbypdXe@' + request.strip() + '" ' + '--form files=@"' + marketplace_name + '.zip"')
            os.system('cp ' + marketplace_name + '.zip /build_archives')
            os.system('rm ' + marketplace_name + '.zip')
        cd('../../..')
        os.system('pwd')
        os.system('echo $BB_AUTH_STRING')
        os.system('zip -r aw_m2_' + result_name + '.community_edition.zip app')
        ce = '"aw_m2_' + result_name + '.community_edition.zip"'
        os.system('zip -r aw_m2_' + result_name + '.enterprise_edition.zip app')
        ee = '"aw_m2_' + result_name + '.enterprise_edition.zip"'
        os.system("cp " + ce + " /build_archives")
        os.system("cp " + ee + " /build_archives")
        os.system(
            'curl -X POST "https://IgorSednev:FAdCM9dzPXzMYsbypdXe@' + request.strip() + '" ' + '--form files=@"' + ce + '"')
        os.system(
            'curl -X POST "https://IgorSednev:FAdCM9dzPXzMYsbypdXe@' + request.strip() + '" ' + '--form files=@"' + ee + '"')

    def add_license_to_php_files(self, path, license_template):
        with cd(path):
            with open(path + '/composer.json') as f:
                composer = json.load(f)
            with open(path + "/registration.php") as reg:
                l = reg.readlines()
                for line in l:
                    if line.find("Aheadworks_") != -1:
                        package_name = line.split("_")[1][:-2]

            license_template = license_template.replace("<PACKAGE_NAME>", package_name[:-1])
            license_template = license_template.replace("<VERSION>", composer["version"])
            license_template = license_template.replace("<COPYRIGHT_YEAR>", str(datetime.now().year))

            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith(".php"):
                        with open(os.path.join(root, file)) as f:
                            original_lines = f.readlines()
                        result_lines = list()
                        if len(original_lines):
                            result_lines.append(original_lines[0])
                            result_lines.append(license_template)
                        else:
                            print('WARNING: file ' + os.path.join(root, file) + " is empty")
                        for line in original_lines[1:]:
                            result_lines.append(line)
                        result = open(os.path.join(root, file), 'w')
                        result.writelines([item for item in result_lines])
                        result.close()

    def make_archive(self, source, destination):
        base = os.path.basename(destination)
        name = base.split('.')[0]
        format = base.split('.')[-1]
        archive_from = os.path.dirname(source)
        archive_to = os.path.basename(source.strip(os.sep))
        shutil.make_archive(name, format, archive_from, archive_to)
        shutil.move('%s.%s' % (name, format), destination)

    def find_all(self, name, path):
        result = []
        for root, dirs, files in os.walk(path):
            if name in files:
                result.append(os.path.join(root, name))
        return result

    def build_mm_pack(self, bitbucket_workspace, bitbucket_repo_slug):
        # basically marketplace pack is a ecommerce pack where all modules have -subscription postfix in their names
        # so we assume that the ecommerce pack has been built so far
        prebuilt_packages_dir = "/build_archives"
        working_dir = "/tmp/unpack"
        package_dir = "/tmp/packages"
        os.system("rm -rf " + working_dir + " && mkdir -p " + working_dir)
        os.system("rm -rf " + package_dir + " && mkdir -p " + package_dir)
        os.system("ls -l " + prebuilt_packages_dir)
        # Extract all packages first
        for filename in os.listdir(prebuilt_packages_dir):
            package_fullpath = os.path.join(prebuilt_packages_dir, filename)
            # TODO: process *.zip only
            if os.path.isfile(package_fullpath):
                sources_dir = os.path.join(working_dir, filename)
                print(package_fullpath)
                os.system('unzip -q ' + package_fullpath + ' -d ' + sources_dir)

        # Now gather module names
        module_names = []
        composer_files = self.find_all('composer.json', working_dir)
        print(composer_files) # debug
        for composer_file in composer_files:
            package_name = self.json_parser.get_variable_from_file('name', composer_file)
            if not package_name in module_names:
                module_names.append(package_name)

        print(module_names) # debug
        # Replace all found modules names from "vendor/module_name" to "vendor/module_name-subscription"
        # across all composer.json (this includes requires/suggests sections and possibly even more)
        for composer_file in composer_files:
            fin = open(composer_file, "rt")
            data = fin.read()
            fin.close()

            for module_name in module_names:
                # we intentionally quote vendor/package_name string to be "vendor/package_name".
                # otherwise vendor/package_name_subname could be renamed
                # into vendor/package_name-subscription_subname
                # instead of vendor/package_name_subname-subscription
                data = data.replace('"' + module_name + '"', '"' + module_name + '-subscription"')
                fin = open(composer_file, "wt")
                fin.write(data)
                fin.close()

        # Create '-subscription' packages
        for originalname in os.listdir(working_dir):
            split_name, split_extension = os.path.splitext(originalname)
            target_filename = split_name + "-subscription" + split_extension
            sources_fullpath = os.path.join(working_dir, originalname)
            target_fullpath = os.path.join(package_dir, target_filename)
            print(target_fullpath) # debug
            os.system('cd ' + sources_fullpath + ' && zip -qr ' + target_fullpath + ' .')

        # Copy newly built -subscription packages to /build_archives
        os.system('cp ' + package_dir + '/* ' + prebuilt_packages_dir)
