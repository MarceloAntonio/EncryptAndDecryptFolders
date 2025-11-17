import os
from cryptography.fernet import Fernet, InvalidToken
from .clean import Clean

# Function to decrypt files
def Decrypt(path):
    Clean()

    # Checks if the directory exists
    if not os.path.isdir(path):
        print("\nDirectory not found")   
        return

    # Lists the files inside the directory
    files = os.listdir(path)

    # Loop that iterates over the number of files inside the directory
    for i in range(len(files)): 
        file_path = os.path.join(path, files[i])
            
        try:
            # Checks if it's a directory or a file
            if os.path.isdir(file_path):
                print(f"\n{files[i]} is a folder\n\n")

            else:
                # Decrypting
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

        # If the file is already decrypted, it will fall into this exception
        except InvalidToken:
            print(f"\nThe file {files[i]} has already been decrypted.")