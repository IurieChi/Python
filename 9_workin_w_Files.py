#Working with files
from datetime import datetime
import os

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
    








#call function
disply_cwd()
# up_one_directory()
# disply_cwd()
#disply_all_in_dir("python/")
#disply_file("python/")


