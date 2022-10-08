# Script calculates the XIRR for the investment portfolio.
# Calculation is static for the latest date available

import pandas as pd
from pyxirr import xirr
from datetime import date
from set_engine import engine
import move_two_levels_up
from scripts import daily_balance as db
from scripts import irr_calculations as irr


# Create Consolidated Contributions File
########################################
file_1 = pd.read_csv('inputs/user1/contributions_user1_account1.csv')
file_2 = pd.read_csv('inputs/user1/contributions_user1_account2.csv')
total_column = 'Total_Contributions_USD'
cont_out_file = 'outputs/irr_contributions_user1_AllAccounts.csv'

# Concatenate all files
contributions = db.concat_df(file_1, file_2, type=0)
# Turn DataFrame dates to datetime
contributions = irr.change_column_to_datetime(contributions, 'Date')
# Create total column
contributions = db.add_total_column_to_df(contributions, total_column)
# Keep only Date and Total Column
contributions = irr.filter_df_by_column(contributions, [total_column])
# Invert contributions as cashflow inflows and outflows
contributions = irr.invert_df_column_values(contributions, total_column)
# Turn values to integers
contributions = irr.change_column_to_integers(contributions, total_column)
# Sort values by date in ascending order
contributions.sort_index()
# Save output as CSV
contributions.to_csv(cont_out_file, index=True, index_label='Date')


# Create Consolidated Monthly Account Balance
#############################################
file3 = db.create_df('inputs/user1/monthly_account_balance_user1_account1.csv')
file4 = db.create_df('inputs/user1/monthly_account_balance_user1_account2.csv')
sum_col_name = 'Tot_Acct_Portfolio_USD'
balance_out_file = 'outputs/irr_monthly_account_balance_user1_AllAccounts.csv'

# Merge all files
balance = db.concat_df(file3, file4, type=1)
# Create total column
balance = db.add_total_column_to_df(balance, sum_col_name)
# Turn values to integers
balance = balance.astype('int')
# Keep only Date and Total Column
balance = irr.filter_df_by_column(balance, [sum_col_name])
# Save output as CSV
balance.to_csv(balance_out_file, index=True, index_label='Date')


# # Calculate IRR
#################
contrib_csv = 'outputs/irr_contributions_user1_AllAccounts.csv'
balance_csv = 'outputs/irr_monthly_account_balance_user1_AllAccounts.csv'
balance_df = db.create_df(balance_csv)
contributions_df = db.create_df(contrib_csv)
bal_column = 'Tot_Acct_Portfolio_USD'
cont_column = 'Total_Contributions_USD'

# Get las value from DataFrame
a = irr.get_last_row_of_df(balance_df)
# Rename column as contributions column
b = irr.rename_df_column(a, bal_column, cont_column)
# Concatenate into one df
irr_df = pd.concat([contributions_df, b])
# Separate df into two lists
dates, values = irr.split_df_into_two_lists(irr_df, cont_column)
# Pass lists into xirr function
xirr_result = xirr(dates, values)


# Outputs
#########
# Save value to CSV
today = (f'{date.today():%Y-%m-%d}')
data = [today, xirr_result]
df = pd.DataFrame([data], columns=['Date', 'XIRR'])
df.to_csv("outputs/irr_xirr_user1.csv", index=False)

# Save value to MySQL
xirr = db.create_df('outputs/irr_xirr_user1.csv')

xirr.to_sql(
    name='irr_xirr_user1',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
