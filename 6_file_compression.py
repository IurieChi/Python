#file  Compression

# Read in the ASCII art text file smile_art.txt and write it back to a new file 
# that has a smaller file size than the original file. The original smile_art.txt has a file size of 2.757kB

import os
import json


# Encodes as a list of (char, count) tuples
def encodeString(stringVal):
    encodedList =[]
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count += 1
    encodedList.append((prevChar, count))
    return encodedList
# decode String
def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        try:
            decodedStr = decodedStr + item[0] * item[1]
        except:
            print(item)
    return decodedStr

# encode file from text file
def encodeFile(filename, newFileName):
    with open(filename) as f:
        data = encodeString(f.read())
    
    data = [f'{char}|{count}' for char, count in data]
    
    with open(newFileName, 'w') as f: #create new file and wtite json data 
        f.write('~'.join(data))

# call function decodeString function to read
def decodeFile(filename):
    with open(filename) as f:
        data = f.read()
    pairs = data.split('~')
    pairs = [p.split('|') for p in pairs]
    pairs = [(p[0], int(p[1])) for p in pairs]
    return decodeString(pairs)

print(f"Original file size: {os.path.getsize('smile_art.txt')}")
encodeFile('smile_art.txt', 'smile_art_encoded.txt')
print(f'New file size:  {os.path.getsize("smile_art_encoded.txt")}')
print(decodeFile('smile_art_encoded.txt'))