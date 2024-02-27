# https://docs.python.org/3/library/functions.html#open  Python
# https://docs.python.org/3/library/io.html

# open()	A file open function. The open() function returns a file-type object. It must be either immediately associated with a variable so as not to lose it, or read immediately. If it cannot be found, you will receive an IOError notification.
# file	A file name or a name with an address if the file is not located in the directory where the script is located.
# encoding	This argument specifies the encoding in the text mode of reading a file.
# mode	It is a file access type in which a file is opened. Values are shown in the table below.

# Writing to a File:
# write(str): It writes a string or a sequence of bytes to a file (for binary files) and returns the number of characters written to the file.
# writelines(lines): It writes a list of lines without delimiters (such as line breaks) to a file.
# Reading Data from a File:
# read(size): It reads from a file the size amount of data and returns a newline as '\n'. If the size parameter is not specified, it reads up to the end of the file and returns the data that was read. Upon reaching the end of the file, with further reading we get an empty string.
# readline(): It reads a string from the specified position to the end of the string from the file object and returns it. It reads at most n bytes/characters if specified.

# File Mode	Description
# 'r'	Opens a file for reading. If the file is in read mode, the data is not deleted if the file already exists on the system. If there is no such file, then an error occurs. If the file is open in read mode, then writing to it is impossible, it cannot be written or changed.
# 'w'	Opens a file for writing. If the file exists, then its contents are lost. If the file does not exist at all, a new file is created. If the file is open in write mode, then data can only be written to it, it cannot be read.
# 'x'	Creates a new file for writing. If the name of an existing file is specified, an exception will be generated. No data loss will occur in an existing file.
# 'a'	Opens a file to write to the end of the file (append). If the file does not exist, then it is created. The previously added file content does not change.
# 'r+'	Opens a file for reading and writing from the beginning. The file must exist.
# 'w+'	Opens a file for reading and writing. If the file exists, then its contents are lost.
# 'a+'	Opens a file for reading and writing at the end of the file, appending to the file. If the file does not exist, then it is created.
# Combinations of the above literals can also be appended with:
# "t" – opens a file in text mode, can be omitted
# "b" – opens a file in binary mode

# The following access modes are possible: 'wb', 'rb', 'wb+', 'rb+', etc. If the mode is not specified, then a file is opened in 'rt' mode.
# After working with a file, access to it must be closed using the function file_object.close()

# Another way to close a file is by using the with statement, which closes the file when the block inside the with statement is exited.
# In this case, we don't need to explicitly call the close() method. It is done internally.

# As you already know, to write data to a file in Python, we need to open it in one of the possible write modes w, append or exclusively create x; and to read a file, we have to open the file in read mode r. Various built-in methods are available for this.
# Writing to a File:
# write(str): It writes a string or a sequence of bytes to a file (for binary files) and returns the number of characters written to the file.
# writelines(lines): It writes a list of lines without delimiters (such as line breaks) to a file.
# Reading Data from a File:
# read(size): It reads from a file the size amount of data and returns a newline as '\n'. If the size parameter is not specified, it reads up to the end of the file and returns the data that was read. Upon reaching the end of the file, with further reading we get an empty string.
# readline(): It reads a string from the specified position to the end of the string from the file object and returns it. It reads at most n bytes/characters if specified.

# We can read a file line-by-line using a for loop. This is both efficient and fast.




# with open("my_information.txt",'w',encoding='utf-8') as my_file:
#     my_file.write("Name is Tom Hardy.\n")
#     my_file.write("I am an English actor and producer.\n")
#     my_file.write("I am active in charity work.\n")
# with open("my_information.txt",'r',encoding='utf-8') as my_file:
#     print(my_file.readline())
#     print(my_file.readlines())

# As in C, Python has the current cursor in the file (position), and all operations with data in the file will be performed starting from that position. We can change the current position in the file using the seek(offset[, from]) method. The offset argument indicates the number of bytes to be moved. The from argument specifies the reference position from where the bytes are to be moved:
# SEEK_SET	0	The offset is performed from the beginning of the file. The offset should be zero or positive.
# SEEK_CUR	1	The offset is performed from the current cursor position. The offset may be negative.
# SEEK_END	2	The offset is performed from the end of the file. The offset is usually negative.
# And to find out the current position, we can use the tell() method.
# Let us look at changing the position of the cursor in our example:
# with open("my_information.txt",'w',encoding=  'utf-8') as my_file:
#     my_file.write("Name is Tom Hardy.\n")
#     my_file.write("I am an English actor and a producer.\n")
#     my_file.write("I am active in charity work.\n")
# with open("my_information.txt",'r',encoding='utf-8') as my_file:
#     print(my_file.readline())
#     my_file.seek(0, 0)
#     print(my_file.readlines())

# The result:
# Name is Tom Hardy.
 
# ['Name is Tom Hardy.\n', 'I am an English actor and a producer.\n', 'I am active in charity work.\n']
# In this case, the first line will be displayed twice.

#Working with files
from datetime import datetime
import os, glob

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

#overwrite new content in file and remove ald one 
def write_new_content(name, content):
    with open(name, 'w') as f:
        f.write(content)
    read_file(name) # call function to read file 

#Add new contet to file 
def write_new_content_apend(name, content):
    with open(name, 'a') as f:
        f.write(content)
    read_file(name) # call function to read file 


#call function
# disply_cwd()
# up_one_directory()
# disply_cwd()
# disply_all_in_dir("artwork/")
# disply_file("Python /")
# search_by_file_name('*fibonaci*')
# display_ext("*.txt")
# display_ext("*.py")
# find_file_in_subDirectories('**/*fibonaci*')

# read_file('smile_art.txt')
# write_new_content('a.txt','This is some text new information added')
# write_new_content_apend('a.txt','\n new information added')

#read_file_line_by_line("a.txt")

# For instance, consider the example in which we open a text file to record information about ourselves in the future:in C language
# #include <stdio.h> 
# #include <stdlib.h>  
 
# int main() 
# { 
#     FILE  *fileName = fopen("my_information.txt", "w+t"); 
#     if(fileName == NULL) 
#     { 
#         printf("Error. Could not open or unable to create a file.\n");     
#         return 0; 
#     } else 
#         printf("The file is opened successfully.\n"); 
 
#     //some block of code 
 
#     fclose(fileName); 
#     return 0; 
# }


# Node.js provides the fs core module that presents the functions to work with a file system. You can find the documentation here (https://nodejs.org/api/fs.html).


# To open a file, we will use the fs.promises.open method that returns a file handler.
# fs.promises.open(path, flags)
# Parameter	Description
# path	A file path that should be opened.
# flags	It is a file access type in which a file is opened. Values are shown in the table below.
# File Access Type Table:
# File Mode	Description
# 'r'	Opens a file for reading. If the file is in read mode, the data is not deleted in case the file already exists in the system. If there is no such file, then an error occurs. If the file is open in read mode, then writing to it is impossible; it cannot be written or changed.
# 'w'	Opens a file for writing. If the file exists, then its contents are lost. If the file does not exist at all, a new file is created. If the file is open in write mode, then data can only be written to it and it cannot be read.
# 'x'	Creates a new file for writing. If the name of an existing file is specified, an exception will be generated. No data loss will occur in the existing file.
# 'a'	Opens a file to write to the end of the file (append). If the file does not exist, then it is created. The content of the previously added file does not change.
# 'r+'	Opens a file for reading and writing from the beginning. The file must exist.
# 'w+'	Opens a file for reading and writing. If the file exists, then its contents are lost.
# 'a+'	Opens a file for reading and writing at the end of the file, appending to the file. If the file does not exist, then it is created.

# g