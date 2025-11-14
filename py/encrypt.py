import os
from cryptography.fernet import Fernet
from .GenKey import GenKey
from .clean import Clean
from time import sleep
def Encrypt(path):
    Clean()
    confirm = input(f"\nAre you sure you want to encrypt the following path?\n\n {path}\n\n yes[Y] - no[N]\nOption: ")
    if confirm not in ("y","Y"):
      print("\nAborting encryption")
      return
  
  
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
        print("generated key!\n")
        sleep(0.5)

    try:
          files = os.listdir(path)

          for i in range(len(files)): 
              file_path = os.path.join(path, files[i])
              try:
                  if os.path.isfile(file_path):
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
                  else:
                      print(f"\n{files[i]} is a folder\n\n")
              except:
                  print("\nNo permission to access the file")
    except:
          print("\nDirectory not found")
      

