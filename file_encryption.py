# Script checks user input files to check they are correct.
import os
import sys
from scripts import encryption as en

# Get username
user = sys.argv[1]
print('\nSelected user: ', sys.argv[1], '\n')

# Get user filepath
user_dir = ('./inputs/' + user + '/')
print('Selected user directory: ', user_dir, '\n')

# Find files in filepath
user_files = os.listdir(user_dir)
print('Files in directory:\n', user_files, '\n')

# Get user password
o_user = en.Cryptography()
o_user.get_password()
o_user.generate_key(o_user.password)

# Encrypt or decrypt
instruction = sys.argv[2]
if instruction == 'encrypt':
    # Encrypt files
    for file in user_files:
        o_user.encrypt_file(user_dir+file, user_dir+file)
elif instruction == 'decrypt':
    # Decrypt files
    try:
        for file in user_files:
            o_user.decrypt_file(user_dir+file, user_dir+file)
    except Exception:
        print('\nInvalid Password\n')
