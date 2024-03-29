# Script to calculate the daily balance of the portfolio
# for every day within the investment period.

from set_engine import engine
import move_two_levels_up
from scripts import daily_balance as db
from set_analysis_dates import date_range


# GBM Account
#############
# Get monthly balance
balance_df1 = db.create_df('inputs/pcl/monthly_account_balance_PCL_GBM.csv')

# Create daily balance
daily_balance_df1 = db.create_daily_balance_df(
    df=balance_df1,
    column_name='Tot_Acct_GBM_MXN',
    sum=False,
    range=date_range)

# Output to CSV
filename1 = 'outputs/daily_acct_balance_PCL_GBM.csv'
daily_balance_df1.to_csv(filename1, index=True, index_label='Date')

# Output to MySQL
daily_balance_df1.to_sql(
    name='daily_acct_balance_PCL_GBM',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# CETES Account
###############
# Get monthly balance
balance_df2 = db.create_df('inputs/pcl/monthly_account_balance_PCL_CETES.csv')

# Create daily balance
daily_balance_df2 = db.create_daily_balance_df(
    df=balance_df2,
    column_name='Tot_Acct_Cetes_MXN',
    sum=False,
    range=date_range)

# Output to CSV
filename2 = 'outputs/daily_acct_balance_PCL_CETES.csv'
daily_balance_df2.to_csv(filename2, index=True, index_label='Date')

# Output to MySQL
daily_balance_df2.to_sql(
    name='daily_acct_balance_PCL_CETES',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# IBKR Account
##############
# Get monthly balance
balance_df3 = db.create_df('inputs/pcl/monthly_account_balance_PCL_IBKR.csv')

# Create daily balance
daily_balance_df3 = db.create_daily_balance_df(
    df=balance_df3,
    column_name='Tot_Acct_IBKR_MXN',
    sum=False,
    range=date_range)

# Output to CSV
filename3 = 'outputs/daily_acct_balance_PCL_IBKR.csv'
daily_balance_df3.to_csv(filename3, index=True, index_label='Date')

# Output to MySQL
daily_balance_df3.to_sql(
    name='daily_acct_balance_PCL_IBKR',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# Sum All Accounts
##################
acct_1 = db.create_df('outputs/daily_acct_balance_PCL_CETES.csv')
acct_2 = db.create_df('outputs/daily_acct_balance_PCL_GBM.csv')
acct_3 = db.create_df('outputs/daily_acct_balance_PCL_IBKR.csv')

added_df = db.concat_df(acct_1, acct_2, acct_3, type=1)
total_balance_df = db.add_total_column_to_df(added_df, 'Tot_Acct_Portafolio_MXN')

# Output to CSV
filename4 = 'outputs/daily_acct_balance_PCL_AllAccounts.csv'
total_balance_df.to_csv(filename4, index=True, index_label='Date')

# Output to MySQL
total_balance_df2 = db.create_df(filename4)

total_balance_df2.to_sql(
    name='daily_acct_balance_PCL_AllAccounts',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
