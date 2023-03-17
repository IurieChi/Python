#Move rename copy delete file directory

import os, shutil
from pathlib import Path

#rename file with OS module 
def rename_os(old_name,new_name):
    os.rename(old_name,new_name)

#rename file with pathlib
def rename_pathlib(old_name,new_name):
    file = Path(old_name)
    file.rename(new_name)

#move file with shutil
def move_file_shutil(folder,destinationfolder):
    shutil.move(folder, destinationfolder)

#move file to new directory created
def move_file_in_new_directory(file_name,directory_name):
    os.mkdir(directory_name)
    shutil.move(file_name)

#copy file with shutill without meta data 
def copy_file(file,directory):
    shutil.copy(file,directory)

#copy file with meta data creation data etc.
def copy_file_meta(file,directory):
    shutil.copy2(file,directory)

#copy entyre directory wirh shutil

def copy_directory(source,destination):
    shutil.copytree(source,destination)

#*********** Delete files with python will delete file totaly from PC***********************

def remove_file_os(file):
    os.remove(file)
    #os.unlink(file)

#delete file with pathlib
def delete_file_pathlib(file_name):
    file = Path(file_name)
    file.unlink()

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

#rename_os('a.txt', 'aa.txt')
#move_file_shutil("test/Folder2/png", "test")
#copy_file_meta('test/png/monster01.png','test')

# remove_file_os('test/monster01.png')
# delete_dire_andSub_direct('test/Folder2')

