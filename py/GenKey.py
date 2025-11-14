from cryptography.fernet import Fernet
import os

def GenKey():
  key = Fernet.generate_key()

  with open('FileKey.key', 'wb') as filekey:
    filekey.write(key)
    print(f"\nThe key was created in the following path: {os.getcwd()}\\FileKey.key\n")

if __name__ == "__main__":
    GenKey()