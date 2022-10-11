
import base64
import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Cryptography():

    def __init__(self):
        self.salt = b'\xfai\xed4\xa44!\xd4\x85u1\xb4\xee\xdb<m'

    def getPassword(self):
        self.get_password = getpass.getpass("Enter password: ")
        self.password = self.get_password.encode()

    def generateKey(self, password):
        self.kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=480_000)
        self.key = base64.urlsafe_b64encode(self.kdf.derive(password))
        self.f = Fernet(self.key)

    def encryptFile(self, origin_filename, encrypted_filename):
        with open(origin_filename, 'rb') as file:
            self.original_file = file.read()

        self.encrypted = self.f.encrypt(self.original_file)

        with open(encrypted_filename, 'wb') as file:
            file.write(self.encrypted)

    def decryptFile(self, enc_filename, dec_filename):
        with open(enc_filename, 'rb') as file:
            self.encrypted = file.read()

        self.decrypted = self.f.decrypt(self.encrypted)

        with open(dec_filename, 'wb') as file:
            file.write(self.decrypted)

    # For debugging
    def showState(self):
        print()
        print('Salt is: ', self.salt)
        print('Password is: ', self.get_password)


# Main code
user1 = Cryptography()
user1.getPassword()
user1.generateKey(user1.password)
user1.encryptFile('trade_history.csv', 'encrypted_trade_history.csv')
user1.decryptFile('encrypted_trade_history.csv', 'decrypted_trade_history.csv')
user1.showState()
