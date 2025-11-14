import os
from cryptography.fernet import Fernet, InvalidToken
from .clean import Clean




def Decrypt(path):
    Clean()
    try:
        files = os.listdir(path)

        for i in range(len(files)): 
            file_path = os.path.join(path, files[i])
            try:
                if os.path.isfile(file_path):
                    print(f"\nDecrypting: {files[i]}")  
                    with open("FileKey.key", "rb") as file_key:
                        key = file_key.read()
                        
                    fernet = Fernet(key)

                    with open(file_path, "rb") as encrypted_file:
                        encrypted_data = encrypted_file.read()
                    
                    decrypted_data = fernet.decrypt(encrypted_data)

                    with open(file_path, "wb") as decrypted_file:
                        decrypted_file.write(decrypted_data)
                    print(f"\n{files[i]} has been decrypted")
                else:
                    print(f"\n{files[i]} is a folder\n\n")
            except InvalidToken:
                print(f"\nThe file {files[i]} has already been decrypted.")  
              
        
    except FileNotFoundError:
        print("\nDirectory not found")



