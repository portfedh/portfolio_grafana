import base64
import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Salt
salt = b'\xfai\xed4\xa44!\xd4\x85u1\xb4\xee\xdb<m'
# salt = os.urandom(16)
print('Salt is: ', salt)

# Get password
get_password = getpass.getpass("Enter password: ")

# Make binary
password = get_password.encode()
print('Password is: ', password)

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

# Get Message
with open('trade_history.csv', 'rb') as original_file:
    original = original_file.read()

# Encrypted
encrypted = f.encrypt(original)
print('Encrypted message is: ', encrypted)
with open('enc_v4_trade_history.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

# Decrypted
decrypted = f.decrypt(encrypted)

with open('dec_v4_trade_history.csv', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)