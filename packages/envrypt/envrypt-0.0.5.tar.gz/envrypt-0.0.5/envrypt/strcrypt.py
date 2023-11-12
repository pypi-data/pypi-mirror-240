import os
import sys
import base64

ENCRYPT_KEY = None

ENCRYPT_KEY_FILE = ".envrypt"

if not os.path.exists(ENCRYPT_KEY_FILE):
    print(f"For dev convenience, you can create a {ENCRYPT_KEY_FILE} file with a single line containing the encryption key.")

    # ask user to enter encryption key
    ENCRYPT_KEY = input("Enter encryption key: ").strip()
    if len(ENCRYPT_KEY) < 8:
        print("Encryption key must be at least 8 characters long.")
        sys.exit(1)

if not ENCRYPT_KEY:
    with open(ENCRYPT_KEY_FILE, "r") as f:
        ENCRYPT_KEY = f.read().strip()

def encrypt(text, key=ENCRYPT_KEY):
    """Encrypts a given string using the XOR cipher.
    
    Parameters:
    ----------
    text : str
        The string to be encrypted.
    key : int
        The encryption key.
    """
    rv_bytes = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))
    return to_base64(rv_bytes)


def decrypt(text, key=ENCRYPT_KEY):
    """Decrypts a given string through a given key.
    
    Parameters:
    text : str
        The text to be decrypted.
    key : int
        The key to use for decrypting the string.
    """

    # decode base64
    encrypted_bytes = base64.b64decode(text).decode('utf-8')

    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(encrypted_bytes))


def to_base64(data_bytes):
    """Converts a given bytes object to a base64 string.
    
    Parameters:
    data_bytes : bytes
        The bytes object to convert.
    """
    ascii_encoded = data_bytes.encode('ascii')
    return base64.b64encode(ascii_encoded).decode('utf-8')
