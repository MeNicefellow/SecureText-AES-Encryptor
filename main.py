from endecryptor import *



text = "Hello, World!"
encrypted, key, iv = encrypt(text)
print("Encrypted:", encrypted)
print("Key:", key)
print("IV:", iv)

decrypted = decrypt(encrypted, key, iv)
print("Decrypted:", decrypted)