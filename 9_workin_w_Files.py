#Working with files
from datetime import datetime
import os
import glob

#create time format
def time_format(timestamp):
    formattime=datetime.utcfromtimestamp(timestamp)
    formated_date = formattime.strftime('%d-%m-%y %H:%M:%S')
    return formated_date

#disply curent working directory 
def disply_cwd():
    cwd = os.getcwd()
    print("Curent working directory ",cwd)

#disply only directory not files 
def disply_only_directories(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir():
                print("Directory name", entry.name)
            
#disply only files with is_file
def disply_file(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                print("File name",entry.name)
               
# chenge one up directory 
def up_one_directory():
    os.chdir("../")

def disply_all_in_dir(directory):
    #os.listdir()
    with os.scandir(directory) as entries:
        for entry in entries:
            print(entry.name)
            info= entry.stat()
            # for Mac
            print("Creation time" , time_format(info.st_birthtime))
            # for Windows: print("Creation Time: ", info.st_ctime)
            print("Last access time", time_format(info.st_atime))
            print("Size:",info.st_size)

#display only specific extension of file  like *.txt
def display_ext(extension):
    ext = glob.glob(extension)
    for i in ext:
        print(i)

#disply by file name in dircectory 
def search_by_file_name(name):
    file = glob.glob(name)
    if file:
        for i in file:
            print(i)
    else:
        print(f"File not found with this name :'{name}'")

#disply by file name in subdircectories '**/*file name*'
def find_file_in_subDirectories(name):
    for file in glob.iglob(name, recursive=True):
        print(file)









#call function
disply_cwd()
# up_one_directory()
# disply_cwd()
#disply_all_in_dir("python/")
#disply_file("python/")
search_by_file_name('*fibonaci*')
display_ext("*.txt")
display_ext("*.py")
find_file_in_subDirectories('**/*fibonaci*')


