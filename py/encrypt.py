import os
from cryptography.fernet import Fernet
from .GenKey import GenKey
from .clean import Clean
from time import sleep

def Encrypt(path):
    Clean()

    # Checks if the directory exists
    if not os.path.isdir(path):
        print("\nDirectory not found")   
        return

    # Asks the user for confirmation to be sure they want to encrypt the following directory
    confirm = input(f"\nAre you sure you want to encrypt the following path?\n\n {path}\n\n yes[Y] - no[N]\nOption: ")
    if confirm not in ("y", "Y"):
        print("\nAborting encryption")
        return
  
    # If the key does not exist, it creates one
    if not os.path.exists("FileKey.key"):
        print("Generating key.")
        sleep(0.5)
        Clean()
        print("Generating key..")
        Clean()
        sleep(0.5)
        Clean()
        print("Generating key...")
        sleep(0.5)
        
        Clean()
        GenKey()
        print("Generated key!\n")
        sleep(0.5)

    # Lists what exists inside the directory
    files = os.listdir(path)
    
    # Loop that iterates over the number of files inside the directory
    for i in range(len(files)): 
        file_path = os.path.join(path, files[i])
             
        # Checks if it's a folder
        if os.path.isdir(file_path):
            print(f"\n{files[i]} is a folder\n\n")
             
        else:
            # Encrypting
            print(f"\nEncrypting: {files[i]}")
            with open('FileKey.key', 'rb') as file_key:
                key = file_key.read()
                        
            fernet = Fernet(key)

            with open(file_path, 'rb') as file:
                content = file.read()

            encrypted = fernet.encrypt(content)

            with open(file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)

            print(f"\n{files[i]} has been encrypted\n\n")