import paramiko
import os
import argparse
from cryptography.fernet import Fernet

# Generate or load encryption key
KEY_FILE = "encryption.key"

def generate_key():
    """Generate a new encryption key if not already present."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

def load_key():
    """Load the encryption key from a file."""
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

def encrypt_file(input_file, encrypted_file, key):
    """Encrypt a file using Fernet encryption."""
    cipher = Fernet(key)
    with open(input_file, "rb") as f:
        data = f.read()
    encrypted_data = cipher.encrypt(data)
    with open(encrypted_file, "wb") as f:
        f.write(encrypted_data)
    print(f"✅ Encrypted file saved as: {encrypted_file}")

def transfer_file(encrypted_file, remote_path, hostname, username, password):
    """Transfer encrypted file over SSH using SFTP."""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)

        sftp = ssh.open_sftp()
        sftp.put(encrypted_file, remote_path)
        sftp.close()
        ssh.close()

        print(f"🚀 File successfully transferred to {hostname}:{remote_path}")

    except Exception as e:
        print(f"❌ SSH Transfer failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="Securely transfer encrypted files over SSH.")
    parser.add_argument("file", help="File to encrypt and transfer")
    parser.add_argument("remote_path", help="Remote file path")
    parser.add_argument("hostname", help="SSH server hostname or IP")
    parser.add_argument("username", help="SSH username")
    parser.add_argument("password", help="SSH password")
    
    args = parser.parse_args()

    generate_key()
    key = load_key()

    encrypted_file = args.file + ".enc"
    encrypt_file(args.file, encrypted_file, key)
    transfer_file(encrypted_file, args.remote_path, args.hostname, args.username, args.password)

if __name__ == "__main__":
    main()
