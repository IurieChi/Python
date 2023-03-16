# create folder 

import os
from pathlib import Path

#create patri with os
def make_directory(name):
    try:
        os.mkdir(name)
    except FileExistsError as ex:
        print(f"'{name}' directory already exists")

def make_dire_Path(name):
    dir_path = Path(name)
    dir_path.mkdir(exist_ok=True)


make_directory("new Folder")
make_dire_Path("new Folder2")
