import base64
import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


# Get password
get_password = getpass.getpass("Enter password: ")

# Make binary
password = get_password.encode()
print('Password is: ', password)

# Salt
salt = b'\xfai\xed4\xa44!\xd4\x85u1\xb4\xee\xdb<m'
# salt = os.urandom(16)
print('Salt is: ', salt)

# Create a key
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=480_000,
    )
print('kdf is: ', kdf) 

key = base64.urlsafe_b64encode(kdf.derive(password))
print('key is: ', kdf)

f = Fernet(key)
print('Fernet is: ', f)


# Message
message = b"This is a secret message!"
print('Message is: ', message)

# Encrypted
token = f.encrypt(message)
print('Encrypted message is: ', token)

L = f.decrypt(token)
print('Decrypted message is: ', L)