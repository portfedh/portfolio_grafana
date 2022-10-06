# Script checks user input files to check they are correct.
import os
import sys
import pandas as pd

# Username
user = sys.argv[1]
print('Username: ', sys.argv[1])

# User filepath
user_dir = ('./inputs/' + user + '/')
print('Selected user directory: ', user_dir)

# Files in filepath
user_filepath = os.listdir(user_dir)

# Check if directory is empty:
if len(user_filepath) == 0:
    raise Exception("User input directory is empty")

# Check that all files are csv:
for file in user_filepath:
    if file.endswith('.csv'):
        print('CSV File: ', file)
    elif file.endswith('.DS_Store'):
        print('DS_Store File:', file)
        # .DS_Store are Mac OS system files.
    else:
        raise Exception(file, "is not a CSV file.")

# Check that there is a Contribution file:
if not any(item.startswith('contributions') for item in user_filepath):
    raise Exception("No contributions file found.")

# Check that there is a Monthly Balance file:
if not any(item.startswith('monthly_account_balance') for item in user_filepath):
    raise Exception("No monthly_account_balance file found.")

# Check that there is a Trade History file:
if not any(item.startswith('trade_history') for item in user_filepath):
    raise Exception("No Trade_history file file found.")

# Check that there are no NaN values in CSV files:
for file in user_filepath:
    # Check CSV files only:
    if file.endswith('.csv'):
        # Create a DataFrame from CSV
        df = pd.read_csv(user_dir+file)
        # Check each value in df to see if it's NaN.
        # NaN values are represented as True.
        a = pd.isnull(df)
        # Return True if any values in df are True.
        b = a.values.any()
        print('Nan values in DF: ', b)
        # Raise exception if NaN values are present.
        if b is True:
            raise Exception("NaN values in DF: ", file)

# # Check that Monthly balance files have the same ending date
list = []
for file in user_filepath:
    if file.startswith('monthly_account_balance'):
        print(user_dir + '/' + file)
        df = pd.read_csv(user_dir + '/' + file)
        list.append(df)
date_list = []
for df in list:
    a = df.iloc[-1][0]
    date_list.append(a)
if len(set(date_list)) <= 1:
    print('A-Ok')
