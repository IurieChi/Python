#display file name in order with walk function 

import os

def top_down_walk(directory):
      for dirpath, dirnames, files in os.walk(directory):
            print("Directory:", dirpath)
            print("Includes these directories")
            for dirname in dirnames:
                print(dirname)
            print("Includes these files")
            for filename in files:
                print(filename)
            print()

def bottom_up_walk(directory):
    for dirpath, dirnames, files in os.walk(directory, topdown=False):      
        print("Directory:", dirpath)
        print("Includes these directories")
        for dirname in dirnames:
            print(dirname)
        print("Includes these files")
        for filename in files:
            print(filename)
        print()


#top_down_walk('file/artwork/')
bottom_up_walk('file/artwork/')