# Script to calculate the daily balance of the portfolio for every
# day during the investment period. 

from sqlalchemy import create_engine
from scripts import daily_balance as db

# Connect to MySQL database
##############################################################################
url = 'mysql+pymysql://root:password1@localhost:3306/PCL_database'
engine = create_engine(url)

# GBM Account
##############################################################################
# Get monthly balance
balance_df1 = db.create_df('inputs/pcl/monthly_account_balance_PCL_GBM.csv')

# Create daily balance
daily_balance_df1 = db.daily_balance(
    df=balance_df1,
    column_name='Tot_Acct_GBM_MXN',
    sum=False)

# Output to CSV
filename1 = 'outputs/daily_acct_balance_PCL_GBM.csv'
daily_balance_df1.to_csv(filename1, index=True, index_label='Date')

# Output to MySQL
daily_balance_df1.to_sql(
    name='daily_acct_balance_PCL_GBM',  # Table name
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# CETES Account
##############################################################################
# Get monthly balance
balance_df2 = db.create_df('inputs/pcl/monthly_account_balance_PCL_CETES.csv')

# Create daily balance
daily_balance_df2 = db.daily_balance(
    df=balance_df2,
    column_name='Tot_Acct_Cetes_MXN',
    sum=False)

# Output to CSV
filename2 = 'outputs/daily_acct_balance_PCL_CETES.csv'
daily_balance_df2.to_csv(filename2, index=True, index_label='Date')

# Output to MySQL
daily_balance_df2.to_sql(
    name='daily_acct_balance_PCL_CETES',  # Table name
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# IBKR Account
##############################################################################
# Get monthly balance
balance_df3 = db.create_df('inputs/pcl/monthly_account_balance_PCL_IBKR.csv')

# Create daily balance
daily_balance_df3 = db.daily_balance(
    df=balance_df3,
    column_name='Tot_Acct_IBKR_MXN',
    sum=False)

# Output to CSV
filename3 = 'outputs/daily_acct_balance_PCL_IBKR.csv'
daily_balance_df3.to_csv(filename3, index=True, index_label='Date')

# Output to MySQL
daily_balance_df3.to_sql(
    name='daily_acct_balance_PCL_IBKR',  # Table name
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# Sum All Accounts
##############################################################################
acct_1 = 'outputs/daily_acct_balance_PCL_CETES.csv'
acct_2 = 'outputs/daily_acct_balance_PCL_GBM.csv'
acct_3 = 'outputs/daily_acct_balance_PCL_IBKR.csv'

added_df = db.add_df(acct_1, acct_2, acct_3)
unique_df = db.remove_duplicates(added_df)
total_balance_df = db.add_total_column(unique_df, 'Tot_Acct_Portafolio_MXN')

# Output to CSV
filename4 = 'outputs/daily_acct_balance_PCL_AllAccounts.csv'
total_balance_df.to_csv(filename4, index=False)

# Output to MySQL
total_balance_df2 = db.create_df(filename4)

total_balance_df2.to_sql(
    name='daily_acct_balance_PCL_AllAccounts',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
