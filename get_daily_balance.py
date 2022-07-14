from sqlalchemy import create_engine
from scripts import daily_balance as db

# MySQL Connection Settings
###########################
url = 'mysql+pymysql://root:password1@localhost:3306/PCL_database'
engine = create_engine(url)

"""
# IBKR Account
###############
# Get monthly balance
balance_df3 = db.create_df('inputs/pcl/monthly_account_balance_PCL_IBKR.csv')

# Create daily balance
daily_balance_df3 = db.daily_balance(
    df=balance_df3,
    column_name='Tot_Acct_IBKR_MXN',
    sum=False)

# Output to CSV
filename1 = 'outputs/daily_acct_balance_PCL_IBKR.csv'
daily_balance_df3.to_csv(filename1, index=True, index_label='Date')

# Output to MySQL
daily_balance_df3.to_sql(
    name='daily_acct_balance_PCL_IBKR',  # Table name
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
"""
# CETES Account
###############
# Get monthly balance
balance_df2 = db.create_df('inputs/pcl/monthly_account_balance_PCL_CETES.csv')

# Create daily balance
daily_balance_df2 = db.daily_balance(
    df=balance_df2,
    column_name='Tot_Acct_Cetes_MXN',
    sum=False)

# Output to CSV
filename1 = 'outputs/daily_acct_balance_PCL_CETES.csv'
daily_balance_df2.to_csv(filename1, index=True, index_label='Date')

# Output to MySQL
daily_balance_df2.to_sql(
    name='daily_acct_balance_PCL_CETES',  # Table name
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# GBM Account
#############
# Get monthly balance
balance_df = db.create_df('inputs/pcl/monthly_account_balance_PCL_GBM.csv')

# Create daily balance
daily_balance_df = db.daily_balance(
    df=balance_df,
    column_name='Tot_Acct_GBM_MXN',
    sum=False)

# Output to CSV
filename2 = 'outputs/daily_acct_balance_PCL_GBM.csv'
daily_balance_df.to_csv(filename2, index=True, index_label='Date')

# Output to MySQL
daily_balance_df.to_sql(
    name='daily_acct_balance_PCL_GBM',  # Table name
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# Sum both Accounts
###################
# Get total daily balance
total_balance_df = db.consolidate(
    file_name_1='outputs/daily_acct_balance_PCL_CETES.csv',
    file_name_2='outputs/daily_acct_balance_PCL_GBM.csv',
    sum_col_name='Tot_Acct_Portafolio_MXN')

# Output to CSV
filename3 = 'outputs/daily_acct_balance_PCL_AllAccounts.csv'
total_balance_df.to_csv(filename3, index=False)

# Output to MySQL
total_balance_df2 = db.create_df(filename3)

total_balance_df2.to_sql(
    name='daily_acct_balance_PCL_AllAccounts',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
