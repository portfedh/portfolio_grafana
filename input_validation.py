# Script checks user input files to check they are correct.
import os
import sys
import pandas as pd

# Username
user = sys.argv[1]
print('\nSelected user: ', sys.argv[1], '\n')

# User filepath
user_dir = ('./inputs/' + user + '/')
print('Selected user directory: ', user_dir, '\n')

# Files in filepath
user_files = os.listdir(user_dir)
print('Files in directory:\n', user_files, '\n')

# Check if directory is empty:
if len(user_files) == 0:
    raise Exception("User input directory is empty.\n")

# Check that all files are csv:
print('Checking the input file type:')
for file in user_files:
    if file.endswith('.csv'):
        print('CSV File: ', file)
    elif file.endswith('.DS_Store'):
        print('DS_Store File:', file)
        # .DS_Store are Mac OS system files.
    else:
        raise Exception(file, "is not a CSV file.")
print()

# Check that there is a Contribution file:
print('Checking that there is a contributions file.')
if not any(item.startswith('contributions') for item in user_files):
    raise Exception("No contributions file found.")

# Check that there is a Monthly Balance file:
print('Checking that there is a monthly account balance file.')
if not any(item.startswith('monthly_account_balance') for item in user_files):
    raise Exception("No monthly_account_balance file found.")

# Check that there is a Trade History file:
print('Checking that there is a trade history file.')
if not any(item.startswith('trade_history') for item in user_files):
    raise Exception("No Trade_history file file found.")

# Check that there are no NaN values in CSV files:
print('\nChecking that there are no NaN values in CSV files:')
for file in user_files:
    # Check CSV files only:
    if file.endswith('.csv'):
        # Create a DataFrame from CSV
        df = pd.read_csv(user_dir+file)
        # Check each value in df to see if it's NaN.
        # NaN values are represented as True.
        a = pd.isnull(df)
        # Return True if any values in df are True.
        b = a.values.any()
        print('Nan values in DF: ', file, b)
        # Raise exception if NaN values are present.
        if b is True:
            raise Exception("NaN values found in DF: ", file)

# Check that monthly balance files have the same ending date
print('\nChecking that monthly balances have the same ending date:')
# Filter monthly account balance files.
monthly_account_balance_list = []
for file in os.listdir(user_dir):
    if file.startswith('monthly_account_balance'):
        print(user_dir + '/' + file)
        df = pd.read_csv(user_dir + '/' + file)
        monthly_account_balance_list.append(df)
# Find the first column value in the last row.
# Append it to list
date_list = []
for df in monthly_account_balance_list:
    a = df.iloc[-1][0]
    date_list.append(a)
# Check that both dates are equal
if not len(set(date_list)) <= 1:
    raise Exception("Dates do not match").args

print('A-Ok. All files have the same ending date.')
print('Input validation tests Passed.\n')
