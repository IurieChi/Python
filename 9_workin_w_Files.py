#Working with files

import os

#disply curent working directory 
def disply_cwd():
    cwd = os.getcwd()
    print("Curent working directory ",cwd)

# chenge one up directory 
def up_one_directory():
    os.chdir("../")

def disply_all_one_dir(directory):
    #os.listdir()
    with os.scandir(directory) as entries:
        for entry in entries:
            print(entry.name)



#call function
disply_cwd()
up_one_directory()
disply_cwd()
disply_all_one_dir("python/")


