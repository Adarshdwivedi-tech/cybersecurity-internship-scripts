"""
SHA-256 File Hash Generator & Comparator
-------------------------------------------
Generates the SHA-256 hash of two files and checks whether they are
identical. This is commonly used to verify file integrity - for
example, confirming a downloaded file hasn't been corrupted or
tampered with.

Usage:
    Run the script and enter the paths of two files to compare.
"""

import hashlib


def get_hash(filename):
    """Reads a file in chunks and returns its SHA-256 hex digest."""
    h = hashlib.sha256()

    with open(filename, "rb") as f:
        while chunk := f.read(4096):
            h.update(chunk)

    return h.hexdigest()


file1 = input("Enter first file: ")
file2 = input("Enter second file: ")

hash1 = get_hash(file1)
hash2 = get_hash(file2)

print("\nHash of File1:", hash1)
print("Hash of File2:", hash2)

if hash1 == hash2:
    print("\nFiles are identical")
else:
    print("\nFiles are different")
