# create folder 


import os,shutil
from pathlib import Path
import  sys
class Folder:

#create patri with os
    def make_directory(name):
        try:
            os.mkdir(name)
        except FileExistsError as ex:
            print(f"'{name}' directory already exists")

    def make_dire_Path(name):
        dir_path = Path(name)
        dir_path.mkdir(exist_ok=True)


    #*********** Delete files with python will delete file totaly from PC***********************
    #delete directory with os module
    def delete_directory_os(directory):
        os.rmdir(directory)

    def delte_directory_pathlib(directory):
        direct = Path(directory)
        direct.rmdir()

    #delete directory including subdirectory
    def delete_dire_andSub_direct(directory):
        shutil.rmtree(directory)

#*********** Delete files with python will delete file totaly from PC***********************
folder = Folder()
# folder.make_directory("PDF")
# folder.make_dire_Path("pdf")

# remove_file_os('test/monster01.png')
# delete_dire_andSub_direct('test/Folder2')

# print(os.listdir(os.getcwd()))
print(os.stat('somefile.txt'))