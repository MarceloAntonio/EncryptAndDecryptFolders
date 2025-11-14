# EncryptAndDecryptFolders

This project allows you to encrypt and decrypt files inside a folder using Python, with or without Docker.

---

## Using Docker

### 1. Build and start the container
```bash
docker-compose up -d --build
````

### 2. Access the container

```bash
docker exec -it EncryptAndDecryptFolders bash
```

---

## Without Docker

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Show help

```bash
python main.py -h
```

---

## Encrypting Files

```bash
python main.py path -e
```

Example:

```bash
python main.py Test/ -e
```

---

## Decrypting Files

```bash
python main.py path -d
```

Example:

```bash
python main.py Test/ -d
```

