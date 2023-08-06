import os
import shutil, errno

class FileManager:

    def remove_files_and_dirs_ignore_case(self, path, files_to_remove, dirs_to_remove):
        for f in os.listdir(path):
            f_path = os.path.join(path, f)
            if os.path.isfile(f_path) and f.lower() in files_to_remove:
                os.remove(f_path)

            if os.path.isdir(f_path) and f.lower() in dirs_to_remove:
                os.system('rm -rf ' + f_path)

    def create_dir_by_path(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def create_empty_dir(self, path):
        os.system(f"rm -rf {path} && mkdir -p {path}")

    def find_all(self, name, path):
        """ Recoursively find all files in path by name.
        """
        result = []
        for root, dirs, files in os.walk(path):
            if name in files:
                result.append(os.path.join(root, name))
        return result

    def add_license_to_php_files(self, path, license_text):
        # TODO: check if add_info_to_file_header could do this
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".php"):
                    with open(os.path.join(root, file)) as f:
                        original_lines = f.readlines()
                    result_lines = list()
                    if len(original_lines):
                        result_lines.append(original_lines[0])
                        result_lines.append(license_text)
                    else:
                        print(f'WARNING: file {os.path.join(root, file)} is empty')
                    for line in original_lines[1:]:
                        result_lines.append(line)
                    result = open(os.path.join(root, file), 'w')
                    result.writelines([item for item in result_lines])
                    result.close()
