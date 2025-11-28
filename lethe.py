import argparse
from py.decrypt import Decrypt
import py.encrypt
from py.encrypt import Encrypt
from py.GenKey import GenKey
from py.post import PostFile
from py.colors import alert

def main():
  parser = argparse.ArgumentParser(
    prog="lethe.py",
    description="This project is a robust Python CLI tool designed to recursively encrypt and decrypt entire directory structures. It supports various file formats (Text, PDF, Images, Excel)"
  )

  parser.add_argument("-P","--folderPath",nargs="?", help="Path to the target folder (e.g., ./Test).")
  parser.add_argument("-K","--keyPath", nargs="?",help="Path to the security key file.")
  parser.add_argument('--POST','-p',nargs="?", help='Uploads the key to a URL (PUT request).')
  parser.add_argument('--decrypt','-d',action='store_true', help='Activates Decryption mode.')
  parser.add_argument('--encrypt','-e',action='store_true', help='Activates Encryption mode.')
  parser.add_argument('--genkey','-g',action='store_true', help='Generates a new encryption key.')
  parser.add_argument('--skip','-s',action='store_true', help='	Skips the warning confirmation prompt.')
  
  

  arg = parser.parse_args()
  
  selected = sum([arg.encrypt,arg.decrypt])

  if arg.skip:
    py.encrypt.warningTrigger = False

  if selected > 1:
    print(f"{alert} Only one action option can be selected at a time. Try using only -e or -d.")
    return
    
  if arg.genkey:
    GenKey()

  if arg.encrypt:
    Encrypt(arg.folderPath,arg.keyPath)

  elif arg.decrypt:
    Decrypt(arg.folderPath,arg.keyPath)
    
  else:
    print(f"{alert} No encryption or decryption function was selected.")
  

  if arg.POST:
    PostFile(arg.keyPath, arg.POST)


if __name__ == "__main__":
  main()