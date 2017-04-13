import os


class FilesTools(object):
    def get_files_list(self, files_path):
        files = []
        for filename in os.listdir(files_path):
            files.append(filename)
            print('读取文件:', filename)
        return files
