# Script checks user input files to check they are correct.
import os
import sys


# Name of user files
user = sys.argv[1]
print('Username: ', sys.argv[1])


# User filepath
user_dir = ('./inputs/' + user + '/')
print('user_dir: ', user_dir)


# Check if directory is empty
if len(os.listdir(user_dir)) == 0:
    raise Exception("User input directory is empty")
else:
    print("Directory is not empty")

# Check that all files are csv:
# .DS_Store are MacOs system files
for file in os.listdir(user_dir):
    if file.endswith('.csv'):
        print('Found CSV File: ', file)
    elif file.endswith('.DS_Store'):
        print('Found DS_Store File:', file)
    else:
        raise Exception(file, "is not a CSV file.")


# Make a list of the files in directory
dir_list = []
for file in os.listdir(user_dir):
    dir_list.append(file)


# Check that there is a Contribution file.
if not any(item.startswith('contributions') for item in dir_list):
    raise Exception("No contributions file found.")


# Check that there is a Monthly Balance file.
if not any(item.startswith('monthly_account_balance') for item in dir_list):
    raise Exception("No monthly_account_balance file found.")


# Check that there is a Trade History file.
if not any(item.startswith('trade_history') for item in dir_list):
    raise Exception("No Trade_history file file found.")


# Tests that there are no NaN values in input DF.
for file in os.listdir(user_dir):
    if file.endswith('.csv'):
        df = pd.read_csv(user_dir+file)
        a = pd.isnull(df)
        b = a.values.any()
        print('Nan values in DF: ', b)
        if b == True:
            raise Exception("Nan values in DF: ", file)

# # Check that Monthly balance files have the same ending date
list = []
for file in os.listdir(user_dir):
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
