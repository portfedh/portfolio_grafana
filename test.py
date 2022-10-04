# Check user input files

# Add raise statements 


import os
import csv
import pandas as pd

# Check that there is at least one account:
#     -Contributions file
#     -Monthly balance file
#     -Trade history file

path = os.path.dirname('./inputs/user1/')
for file in os.listdir(path):
    if file.startswith('contributions'):
        print('Found a contributions file.')
    if file.startswith('monthly_account_balance'):
        print('Found a monthly_account_balance file.')
    if file.startswith('trade_history'):
        print('Found a trade_history file.')
    else:
        print('Input file missing.')


# Check that all files are csv:
for file in os.listdir(path):
    if file.endswith('.csv'):
        print('Found a CSV File.')
    elif file.endswith('.DS_Store'):
        print('Found a DS_Store File.')
    else:
        print(file, 'is not a CSV file.')


# Check that csv files have no missing values
print('checking non null values')

df = pd.read_csv("./inputs/user1/test.csv")
a = pd.isnull(df)
print(a)

b = pd.isnull(df).values.any()
print('Nan values in DF: ', b)

if pd.isnull(df).any:
    print('if positive')
else:
    print('if negetive')
