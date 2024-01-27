# SecureText AES Encryptor

SecureText AES Encryptor is a Python-based utility for encrypting and decrypting text using the Advanced Encryption Standard (AES). It is designed to be easy to use while providing a high level of security, suitable for a variety of applications where data confidentiality is essential.

## Features

- **AES-256 Encryption**: Utilizes AES with a 256-bit key for encryption, providing robust security.
- **Automatic Key Generation**: Capable of generating a secure, random key if none is provided.
- **Initialization Vector (IV)**: Uses a random IV for each encryption operation, enhancing security.
- **Padding**: Implements PKCS7 padding to support text of any length.
- **Easy to Use**: Simple functions for encrypting and decrypting text.

## Installation

Before running the SecureText AES Encryptor, you need to install the required Python library:

```bash
pip install cryptography
```

## Usage

### Importing the Module

First, import the functions from the script (assuming it's named `securetext_aes_encryptor.py`):

```python
from endecryptor import *
```

### Encrypting Text

To encrypt text:

```python
text = "Your text here"
encrypted, key, iv = encrypt(text)
```

If you do not provide a key, the `encrypt` function will generate one for you.

### Decrypting Text

To decrypt the text, use the same key and IV:

```python
decrypted_text = decrypt(encrypted, key, iv)
```

## Example

```python
text = "Hello, World!"
encrypted, key, iv = encrypt(text)
print("Encrypted:", encrypted)
print("Key:", key)
print("IV:", iv)

decrypted = decrypt(encrypted, key, iv)
print("Decrypted:", decrypted)
```

## Security Notes

- Keep the encryption key and IV secure. Loss of these components can lead to the inability to decrypt your data.
- AES-256 is a strong encryption standard, but the overall security also depends on the safe handling of the key and IV.
- This tool is designed for general purposes. If you're handling extremely sensitive information, consult with a security expert.

## License

Apache 2.0
