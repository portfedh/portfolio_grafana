from cryptography.fernet import Fernet

# Generate key
# ------------
key = Fernet.generate_key()

# Save as file
with open('mykey', 'wb') as mykey:
    mykey.write(key)


# Encrypt a file
# --------------

with open('mykey', 'rb') as mykey:
    key = mykey.read()

f = Fernet(key)

with open('trade_history.csv', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open('enc_trade_history.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

# Decrypt a file
# --------------
with open('mykey', 'rb') as mykey:
    key = mykey.read()

print(key)

f = Fernet(key)

with open('enc_trade_history.csv', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_trade_history.csv', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)
