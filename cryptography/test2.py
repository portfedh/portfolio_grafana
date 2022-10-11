import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Set password
password = b"password"
print('Password is: ', password)

# Salt
salt = os.urandom(16)
print('Salt is: ', salt)

# Dunno
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=480_000,)

# Dunno
key = base64.urlsafe_b64encode(kdf.derive(password))

# Create a key
f = Fernet(key)

token = f.encrypt(b"Secret message!")
print('encrypted message', token)

L = f.decrypt(token)
print('Decrypted message', L)