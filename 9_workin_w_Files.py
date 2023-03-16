#Working with files
from datetime import datetime
import os, glob, json, csv 
# import pandas as pd 



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


#read file from curent directory
def read_file(name):
    with open(name, 'r') as f:
        contents =f.read() #we can read data from file by bytes just need to add bytes in ()
        print(contents)

#function to read lines 
def read_file_in_line(name):
    with open(name) as f:
        line = f.readlines()
        print(line[1])

# read line by line with while
def read_file_line_by_line(name):
    with open(name) as f:
        line = f.readline()
        while line != "":
            print(line)
            line = f.readline()

#write new content in file and remove ald one 
def write_new_content(name, content):
    with open(name, 'w') as f:
        f.write(content)
    read_file(name) # call function to read file 

#read JASON file with json library
def display_json(name):
    with open(name) as f:
        content = json.load(f)
        print(content)

#read specific key from file 
def disply_key_jason(name, key):
    with open(name) as f:
        content = json.load(f)
        print("Welcome ", content[key])


#read csv file usinf csv or panda 
# to install pandas >>pip3 install pandas
def read_csv_read(name):
    with open(name) as f:
        read = csv.reader(f, delimiter=",")
        for row in read:
            print(row) # can add index to read only one index [1]

#read csv with csv.Dictreader
def read_csv_dic(name):
    with open(name) as f:
        dictreader = csv.DictReader(f, delimiter=",")
        for row in dictreader:
            print(f'{row["monsterName"]} is price {row["price"]}')

# read csv with panda module
#ToDo cant import panda to be cheked >>>>>>>
# def read_csv_pandas(name):
# 	df = pd.read_csv(name)
# 	print(df)        


        

#call function
disply_cwd()
# up_one_directory()
# disply_cwd()
# disply_all_in_dir("artwork/")
# disply_file("Python /")
# search_by_file_name('*fibonaci*')
# display_ext("*.txt")
# display_ext("*.py")
# find_file_in_subDirectories('**/*fibonaci*')

#read_file('smile_art.txt')
# write_new_content('a.txt','This is some text new information added')

#read_file_line_by_line("a.txt")

# display_json('monster.json')
# disply_key_jason('monster.json','monsterName')

# read_csv_read('monsters.csv')
read_csv_dic('monsters.csv')
