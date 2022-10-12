
import base64
import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Cryptography():

    def __init__(self):
        self.salt = b'\xfai\xed4\xa44!\xd4\x85u1\xb4\xee\xdb<m'

    def get_password(self):
        self.get_password = getpass.getpass("Enter password: ")
        self.password = self.get_password.encode()

    def generate_key(self, password):
        self.kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=480_000)
        self.key = base64.urlsafe_b64encode(self.kdf.derive(password))
        self.f = Fernet(self.key)

    def encrypt_file(self, origin_filename, encrypted_filename):
        with open(origin_filename, 'rb') as file:
            self.original_file = file.read()

        self.encrypted = self.f.encrypt(self.original_file)

        with open(encrypted_filename, 'wb') as file:
            file.write(self.encrypted)

    def decrypt_file(self, enc_filename, dec_filename):
        with open(enc_filename, 'rb') as file:
            self.encrypted = file.read()

        self.decrypted = self.f.decrypt(self.encrypted)

        with open(dec_filename, 'wb') as file:
            file.write(self.decrypted)

    def show_state(self):
        # For debugging
        print()
        print('Salt is: ', self.salt)
        print('Password is: ', self.get_password)


if __name__ == '__main__':

    # Test code: Requires file named 'plain_text.csv'
    user1 = Cryptography()
    user1.get_password()
    user1.generate_key(user1.password)
    user1.encrypt_file('plain_text.csv', 'cipher_text.csv')
    user1.decrypt_file('cipher_text.csv', 'deciphered_text.csv')
    user1.show_state()
