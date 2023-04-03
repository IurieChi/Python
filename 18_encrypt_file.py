# to be able to encript and decript file need pip install cryptography
from cryptography.fernet import Fernet


def generate_key():
 #generate a key and save it on file 
    key = Fernet.generate_key()
    with open('mykey.txt','wb') as file: 
        file.write(key)

def encryptFile(file):
    with open('mykey.txt','rb')as f:
        key = f.read()
    
    f_object = Fernet(key)# create Fernet ogbbect with our key 
    #read file 
    with open(file, 'rb')as original_file:
        file = original_file.read()
    encrypted = f_object.encrypt(file)
    # save it to file 
    with open('enccrypted.txt', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

def decryptFile(file):
    with open ('mykey.txt', 'rb')as f:
          key =f.read()
    f= Fernet(key)
    with open(file, 'rb')as file:
        encrypted =file.read()
    decrypted = f.decrypt(encrypted)

    with open("decrypted_file.txt", 'wb')as f:
         f.write(decrypted)

     
    
# generate_key()
# encryptFile('files/a.txt')
decryptFile('enccrypted.txt')