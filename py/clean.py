import os

def Clean():
  clear = "cls" if os.name == "nt" else "clear"
  os.system(clear)