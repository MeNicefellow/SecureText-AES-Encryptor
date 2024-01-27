from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def generate_key():
    # Generate a random 256-bit (32 bytes) key
    return os.urandom(32)

def encrypt(text, key=None):
    if key is None:
        key = generate_key()

    # Padding the text to ensure it's a multiple of 128 bits (16 bytes)
    padder = padding.PKCS7(128).padder()
    padded_text = padder.update(text.encode()) + padder.finalize()

    # Create a random 128-bit (16 bytes) IV and encrypt
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_text = encryptor.update(padded_text) + encryptor.finalize()

    return encrypted_text, key, iv

def decrypt(encrypted_text, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_text = decryptor.update(encrypted_text) + decryptor.finalize()

    # Unpadding the text
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_text = unpadder.update(decrypted_padded_text) + unpadder.finalize()

    return decrypted_text.decode()