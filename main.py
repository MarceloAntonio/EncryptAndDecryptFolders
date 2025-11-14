import argparse
from py.decrypt import Decrypt
from py.encrypt import Encrypt

def main():
  parser = argparse.ArgumentParser(
    prog="encryptAnddecryptFolders",
    description="This program can encrypt and decrypt a folder."
  )

  parser.add_argument("folderPath", help="path to the folder you want to encrypt/decrypt")
  parser.add_argument('--decrypt','-d',action='store_true', help='Decrypt')
  parser.add_argument('--encrypt','-e',action='store_true', help='Encrypt')

  arg = parser.parse_args()

  if arg.encrypt:
    Encrypt(arg.folderPath)

  elif arg.decrypt:
    Decrypt(arg.folderPath)
    
  else:
    print("No options selected. Use -h to see the options.")
  
if __name__ == "__main__":
  main()