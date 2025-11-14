FROM python:latest

COPY . /EncryptAndDecryptFolders 

WORKDIR /EncryptAndDecryptFolders 

CMD [ "pip install -r requirements.txt" ]

