# Script to calculate the daily balance of the portfolio
# for every day within the investment period.

from set_engine import engine
from scripts import daily_balance as db

# GBM Account
##############################################################################
# Get monthly balance
balance_df1 = db.create_df('inputs/clg/monthly_account_balance_CLG_GBM.csv')

# Create daily balance
daily_balance_df1 = db.daily_balance(
    df=balance_df1,
    column_name='Tot_Acct_GBM_MXN',
    sum=False)

# Output to CSV
filename1 = 'outputs/daily_acct_balance_CLG_GBM.csv'
daily_balance_df1.to_csv(filename1, index=True, index_label='Date')

# Output to MySQL
daily_balance_df1.to_sql(
    name='daily_acct_balance_CLG_GBM',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# CETES Account
##############################################################################
# Get monthly balance
balance_df2 = db.create_df('inputs/clg/monthly_account_balance_CLG_CETES.csv')

# Create daily balance
daily_balance_df2 = db.daily_balance(
    df=balance_df2,
    column_name='Tot_Acct_Cetes_MXN',
    sum=False)

# Output to CSV
filename2 = 'outputs/daily_acct_balance_CLG_CETES.csv'
daily_balance_df2.to_csv(filename2, index=True, index_label='Date')

# Output to MySQL
daily_balance_df2.to_sql(
    name='daily_acct_balance_CLG_CETES',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# Sum All Accounts
##############################################################################
acct_1 = 'outputs/daily_acct_balance_CLG_CETES.csv'
acct_2 = 'outputs/daily_acct_balance_CLG_GBM.csv'

added_df = db.add_df(acct_1, acct_2)
unique_df = db.remove_duplicates(added_df)
total_balance_df = db.add_total_column(unique_df, 'Tot_Acct_Portafolio_MXN')

# Test function then delete
# # Get total daily balance
# total_balance_df = db.consolidate(
#     file_name_1='outputs/daily_acct_balance_CLG_CETES.csv',
#     file_name_2='outputs/daily_acct_balance_CLG_GBM.csv',
#     sum_col_name='Tot_Acct_Portafolio_MXN')

# Output to CSV
filename3 = 'outputs/daily_acct_balance_CLG_AllAccounts.csv'
total_balance_df.to_csv(filename3, index=False)

# Output to MySQL
total_balance_df2 = db.create_df(filename3)

total_balance_df2.to_sql(
    name='daily_acct_balance_CLG_AllAccounts',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
