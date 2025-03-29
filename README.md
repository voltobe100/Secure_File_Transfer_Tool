# **🔒 Secure File Transfer Tool**

A Python-based tool that **encrypts files** using AES-based **Fernet encryption** before **securely transferring them over SSH**. This ensures data security and integrity during transit.

---

## **✨ Features**

✅ **AES Encryption** – Encrypts files before sending.  
✅ **Secure SSH Transfer** – Uses **SFTP (SSH File Transfer Protocol)**.  
✅ **Automatic Key Management** – Generates an encryption key if not present.  
✅ **Cross-Platform** – Works on Linux, macOS, and Windows.

---

## **📥 Installation**

1️⃣ **Clone the Repository**

```bash
git clone https://github.com/yourusername/secure-file-transfer.git
cd secure-file-transfer
```

2️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## **🚀 Usage**

Run the script to **encrypt and transfer a file**:

```bash
python transfer.py <file> <remote_path> <hostname> <username> <password>
```

**Example:**

```bash
python transfer.py secret.txt /home/user/secret.enc 192.168.1.10 admin mypassword
```

This will:  
✔ Encrypt `secret.txt` → `secret.txt.enc`  
✔ Transfer the encrypted file securely to `192.168.1.10:/home/user/secret.enc`

---

## **🔓 Decrypting on the Remote Server**

On the **receiver’s side**, decrypt the file using Python:

```python
from cryptography.fernet import Fernet

# Load the encryption key
key = open("encryption.key", "rb").read()
cipher = Fernet(key)

# Decrypt the file
encrypted_data = open("secret.enc", "rb").read()
decrypted_data = cipher.decrypt(encrypted_data)

# Save the decrypted file
open("secret.txt", "wb").write(decrypted_data)

print("✅ File successfully decrypted: secret.txt")
```

---

## **🛡️ Security Notes**

🔹 **Do not share `encryption.key` publicly.** It must be transferred securely.  
🔹 **Use SSH key authentication** instead of passwords for better security.  
🔹 **Make sure the SSH server is configured properly** (e.g., port 22 open).

---

## **💡 Example Output**

```bash
$ python transfer.py secret.txt /home/user/secret.enc 192.168.1.10 admin mypassword
✅ Encrypted file saved as: secret.txt.enc
🚀 File successfully transferred to 192.168.1.10:/home/user/secret.enc
```

---

## **📜 License**

This project is licensed under the **MIT License**.

---

### **📌 Contributing**

💡 Found a bug or have an improvement? Feel free to submit a **pull request** or open an **issue**!
