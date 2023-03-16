# count number of files in directory 

import os
from pathlib import Path

#dispaly curent directory
def disply_cwd(): 
    cwd = os.getcwd()
    print("Curent working directory ",cwd)

# will show onli file in curent directory
def count_file_on_directory(directory):
    with os.scandir(directory) as entries:
        count = 0
        for file in entries:
            if file.is_file():
                print("File name" ,file.name)
                count += 1
        print(f"In {directory} exists {count} files")     

# count file in directory and sub directory with os.walk
def count_fileIn_deirectory_subDirectory(path):
    total = 0
    for base, subdires, files in os.walk(path):
        total +=1
    print(f"In directory {path} and subdirectories are {total} files")

#count files with pathlib
def count_files_with_pathlib(path):
    total = 0
    for entry in Path(path).iterdir():
        if entry.is_file():
            total += 1
        else:
            # call function recursivly with folders to check all sub directories
            total += count_files_with_pathlib(entry)
    print(f"In directory {path} and subdirectories are {total} files")
    #return total


#count_file_on_directory("artwork/")
#count_fileIn_deirectory_subDirectory(".")
count_files_with_pathlib(".")
