# Check user input files

import os
import csv
import sys
import pandas as pd


# Check that Monthly balance files have the same ending date
path = os.path.dirname('./inputs/user1/')

list = []
for file in os.listdir(path):
    if file.startswith('monthly_account_balance'):
        print(path + '/' + file)
        df = pd.read_csv(path + '/' + file)
        list.append(df)

date_list = []
for df in list:
    a = df.iloc[-1][0]
    date_list.append(a)

if len(set(date_list)) <= 1:
    print('A-Ok')
