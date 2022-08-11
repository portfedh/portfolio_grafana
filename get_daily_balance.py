from sqlalchemy import create_engine
from scripts import daily_balance as db

# MySQL Connection Settings
###########################
url = 'mysql+pymysql://root:password1@localhost:3306/CLG_database'
engine = create_engine(url)

# CETES Account
###############
# Get monthly balance
balance_df2 = db.create_df('inputs/clg/monthly_account_balance_CLG_CETES.csv')

# Create daily balance
daily_balance_df2 = db.daily_balance(
    df=balance_df2,
    column_name='Tot_Acct_Cetes_MXN',
    sum=False)

# Output to CSV
filename1 = 'outputs/daily_acct_balance_CLG_CETES.csv'
daily_balance_df2.to_csv(filename1, index=True, index_label='Date')

# Output to MySQL
daily_balance_df2.to_sql(
    name='daily_acct_balance_CLG_CETES',  # Table name
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# GBM Account
#############
# Get monthly balance
balance_df = db.create_df('inputs/clg/monthly_account_balance_CLG_GBM.csv')

# Create daily balance
daily_balance_df = db.daily_balance(
    df=balance_df,
    column_name='Tot_Acct_GBM_MXN',
    sum=False)

# Output to CSV
filename2 = 'outputs/daily_acct_balance_CLG_GBM.csv'
daily_balance_df.to_csv(filename2, index=True, index_label='Date')

# Output to MySQL
daily_balance_df.to_sql(
    name='daily_acct_balance_CLG_GBM',  # Table name
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# Sum both Accounts
###################
# Get total daily balance
total_balance_df = db.consolidate(
    file_name_1='outputs/daily_acct_balance_CLG_CETES.csv',
    file_name_2='outputs/daily_acct_balance_CLG_GBM.csv',
    sum_col_name='Tot_Acct_Portafolio_MXN')

# Output to CSV
filename3 = 'outputs/daily_acct_balance_CLG_AllAccounts.csv'
total_balance_df.to_csv(filename3, index=False)

# Output to MySQL
total_balance_df2 = db.create_df(
    'outputs/daily_acct_balance_CLG_AllAccounts.csv')

total_balance_df2.to_sql(
    name='daily_acct_balance_CLG_AllAccounts',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
