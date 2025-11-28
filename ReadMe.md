<div align="center"> <img src="assets/RiverLethe.png" width="70%" alt="Lethe Logo"/> <h1>Lethe</h1>

<p> <b>The river of forgetfulness.</b> </p>

<a href="https://www.python.org/"> <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version"/> </a> <a href="https://docker.com"> <img src="https://img.shields.io/badge/Docker-Ready-2496ED.svg" alt="Docker"/> </a> <a href="LICENSE"> <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"/> </a>

</div>

Named after the river in Greek mythology whose waters caused souls to lose all memory of their past lives, **Lethe** is a tool designed to make your data "forgotten" to unauthorized eyes.

This project is a robust Python CLI tool designed to **recursively encrypt and decrypt** entire directory structures. It supports various file formats (Text, PDF, Images, Excel) and features a remote key upload system.

## Installation & Setup
**Clone repository**
```
git clone https://github.com/MarceloAntonio/Lethe
```
**Going to directory**
```
cd Lethe
```

### Option 1: Isolated Environment

1.  **Build and start the container:**
    ```bash
    docker-compose up -d --build
    ```

2.  **Access the container terminal:**
    ```bash
    docker exec -it lethe bash
    ```

### Option 2: Local Execution

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage Guide

### 1. Generate a Security Key
Before encrypting any files, you must generate a key.

```bash
python lethe.py -g
````

*Output: A file named `FileKey.key` will be created in the root folder.*

### 2\. Encrypt a Folder

Encrypts the target folder recursively.

```bash
# Syntax: python lethe.py -P {folder_path} -K {key_path} -e
python lethe.py -P ./Test -K FileKey.key -e
```

### 3\. Decrypt a Folder

Restores files to their original state.

```bash
# Syntax: python lethe.py -P {folder_path} -K {key_path} -d
python lethe.py -P ./Test -K FileKey.key -d
```

### 4\. Upload Key (HTTP Transfer)

You can send the `.key` file to a remote server. If the upload is successful, **the local key is deleted** for security.

```bash
# Syntax: python lethe.py -K {key_path} -p {TARGET_URL}
python lethe.py -K FileKey.key -p http://localhost:5000/keys/FileKey.key
```

### 5\. Skip Warning

Skips the confirmation prompt.

```bash
python lethe.py -P ./Test -K FileKey.key -e -s
```

-----

## About the HTTP Upload (`-p`)

The `-p` argument allows you to send the key to **any** compatible HTTP server. You don't need a specific software, just an endpoint that meets these requirements:

1.  **Method:** The server must accept **`PUT`** requests.
2.  **Payload:** The script sends the file as **raw binary data** (not `multipart/form-data`).
3.  **URL:** The URL provided must include the final filename (e.g., `.../my_backup.key`).

### Test Server (Included)

Don't have a backend ready? We included a `docker-compose` setup in the `serverUpload` folder so you can test this feature immediately.

It runs a lightweight server (Dufs) configured to accept these uploads.

**To run the test server:**

```bash
cd serverUpload
docker compose up -d
```

*The server will be available at `http://localhost:5000`.*

-----

## Command Reference

| Argument | Long Flag      | Description                                      |
| :------- | :------------- | :----------------------------------------------- |
| `-P`     | `--folderPath` | Path to the target folder (e.g., `./Test`).      |
| `-K`     | `--keyPath`    | Path to the security key file.                   |
| `-g`     | `--genkey`     | Generates a new encryption key.                  |
| `-p`     | `--POST`       | Uploads the key to a URL (PUT request).          |
| `-e`     | `--encrypt`    | Activates **Encryption** mode.                   |
| `-d`     | `--decrypt`    | Activates **Decryption** mode.                   |
| `-s`     | `--skip`       | Skips the warning confirmation prompt.           |
| `-h`     | `--help`       | Displays help message.                           |

-----

## Security Warning

> **DO NOT DRINK FROM THE WRONG WATERS (DO NOT LOSE YOUR KEY).**
>
> 1.  If you encrypt your files and lose the `.key` file, **it is mathematically impossible to recover your data**.
> 2.  When using `-p`, the local key is **deleted** upon success. Ensure your server URL is correct.

-----

## License

This project is open-source. For more details, please read the **[LICENSE](LICENSE)** file.

