"""
File Encryption & Decryption using Fernet (Symmetric Encryption)
------------------------------------------------------------------
Uses the 'cryptography' library's Fernet module to encrypt and then
decrypt a text file. Fernet guarantees that a message encrypted with
it cannot be manipulated or read without the key.

Requirements:
    pip install cryptography

Usage:
    1. Place a file named sample.txt in the same folder as this script.
    2. Run the script. It will:
       - Generate an encryption key (key.key)
       - Encrypt sample.txt -> encrypted.txt
       - Decrypt encrypted.txt -> decrypted.txt
"""

from cryptography.fernet import Fernet
import os

# ---------- ENCRYPTION ----------

# Generate a new encryption key
key = Fernet.generate_key()

with open("key.key", "wb") as key_file:
    key_file.write(key)

cipher = Fernet(key)

# Path to the file you want to encrypt
file_path = "sample.txt"

# Check if the file exists before proceeding
if not os.path.exists(file_path):
    print("File not found!")
    print("Looking for:", file_path)
    exit()

# Read the original file
with open(file_path, "rb") as file:
    data = file.read()

# Encrypt the file contents
encrypted_data = cipher.encrypt(data)

# Save the encrypted version
with open("encrypted.txt", "wb") as file:
    file.write(encrypted_data)

print("File Encrypted Successfully")
print("Key saved as key.key")
print("Encrypted file saved as encrypted.txt")

# ---------- DECRYPTION ----------

# Load the same key used for encryption
with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Read the encrypted file
with open("encrypted.txt", "rb") as file:
    encrypted_data = file.read()

# Decrypt back to original content
decrypted_data = cipher.decrypt(encrypted_data)

# Save the decrypted version
with open("decrypted.txt", "wb") as file:
    file.write(decrypted_data)

print("File Decrypted Successfully")
print("Decrypted file saved as decrypted.txt")
