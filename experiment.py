import hashlib
from cryptography.fernet import Fernet




def encryptKey(filename, key):
    files = Fernet(key)

    with open(filename, "rb") as file:
        #read file_data
        fileData = file.read()

        #Hash the fileData
        hashing = fileData.encode()
       
        hashedData = print("SHA-256:", hashlib.sha256(hashing).hexdigest())

        #Encrypt the hashed fileData
        encryptedData = file.encrypt(hashing)

        #Writing on the encrypted fileData
        with open(filename, "wb") as file:

            file.write(encryptedData)

def decryptKey(filename, key):

    files = Fernet(key)

    with open(filename, "rb")as file:

        #Reads the encrypted data
        encrypted_data = file.read()

        #Decrypts the data
        decrypt_data = files.decrypt(encrypted_data)

        #Writes the Original files
        with open(filename, "wb")as file:
            
            file.write(decrypt_data)

def write_key():

    key = Fernet.generate_key()

    with open("sys.key", "wb")as key_file:
        key_file.write(key)
        

def load_key():
    return open("sys.key", "rb").read()


write_key()

#loading the previous generated key
key = load_key()

file = "revit.txt"

status = file

encryptKey(status,key)

decryptKey(status,key)



