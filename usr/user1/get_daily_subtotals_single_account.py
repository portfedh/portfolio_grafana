# Script to create subtotal amounts from price & quantity data per account

# *** Check if I should column drop Q and P ***

import pandas as pd
from set_engine import engine
import move_two_levels_up
from scripts import daily_balance as db

# Account 1
###########

# Imports
#########
# Import CSV files and create data frames
shares_acc1_df = db.create_df(
    'outputs/daily_share_quantity_user1_account1.csv')
prices_acc1_df = db.create_df(
    'outputs/daily_prices_interpolated_user1_account1.csv')

# Transformations
#################
# Rename columns: Add quantity or price symbol
shares_df = shares_acc1_df.add_prefix('Q_')
prices_df = prices_acc1_df.add_prefix('P_')
# Merge DataFrames
new_df = pd.concat(([shares_df, prices_df]), axis=1)
# Interpolate missing values (prices are NaN on weekend dates)
interpol_acc2_df = new_df.interpolate(
    method='linear', limit_direction='both')

# Subtotal Calculations
########################
# Tickers are hardcoded
# Subtotals ($)
tickers_account1 = ['BND', 'BNDX', 'VTI', 'VXUS']
for x in tickers_account1:
    interpol_acc2_df[f'Sub_{x}'] = (
        interpol_acc2_df[f'Q_{x}'] *
        interpol_acc2_df[f'P_{x}'])

# Outputs
#########
# Output to CSV
filename = 'outputs/daily_subtotals_user1_account1.csv'
interpol_acc2_df.to_csv(filename, index=True, index_label='Date')

# Output to MySQL
table_name = 'daily_subtotals_user1_account1'
interpol_acc2_df.to_sql(name=table_name, con=engine, if_exists='replace',
                         index=True, index_label='Date')

# Account 2
###########

# Imports
#########
# Import CSV files and create data frames
shares_acc2_df = db.create_df(
    'outputs/daily_share_quantity_user1_account2.csv')
prices_acc2_df = db.create_df(
    'outputs/daily_prices_interpolated_user1_account2.csv')

# Transformations
#################
# Rename columns: Add quantity or price symbol
shares_df2 = shares_acc2_df.add_prefix('Q_')
prices_df2 = prices_acc2_df.add_prefix('P_')
# Merge DataFrames
new_df2 = pd.concat(([shares_df2, prices_df2]), axis=1)
# Interpolate missing values (prices are NaN on weekend dates)
interpol_acc2_df = new_df2.interpolate(
    method='linear', limit_direction='both')

# Subtotal Calculations
########################
# Tickers are hardcoded
# Subtotals ($)
tickers_account2 = ['BND', 'BNDX', 'VEA', 'VOO', 'VWO']
for x in tickers_account2:
    interpol_acc2_df[f'Sub_{x}'] = (
        interpol_acc2_df[f'Q_{x}'] *
        interpol_acc2_df[f'P_{x}'])

# Outputs
#########
# Output to CSV
filename = 'outputs/daily_subtotals_user1_account2.csv'
interpol_acc2_df.to_csv(filename, index=True, index_label='Date')

# Output to MySQL
table_name = 'daily_subtotals_user1_account2'
interpol_acc2_df.to_sql(name=table_name, con=engine, if_exists='replace',
                        index=True, index_label='Date')
