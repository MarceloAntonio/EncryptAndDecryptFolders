import requests
import os
from .colors import failure, success

def PostFile(KeyPath, url):
    if os.path.exists(KeyPath):
        try:
            with open(KeyPath, "rb") as f:
                response = requests.put(url, data=f)
            
            if response.status_code in [200, 201]:
                print(f"{success} File transferred")
                os.remove(KeyPath)
            else:
                print(f"{failure} Error {response.status_code}")
                print(response.text)
                
        except Exception as e:
            print(f"{failure} Connection error: {e}")
    else:
        print(f"{failure} The file {KeyPath} does not exist")