from sqlalchemy import create_engine
from scripts import daily_balance as db

# MySQL Connection Settings
##############################################################################
url = 'mysql+pymysql://root:password1@localhost:3306/PCL_database'
engine = create_engine(url)

# GBM Account
##############################################################################
# Get monthly balance
contribution_balance_df1 = db.create_df(
    'inputs/pcl/contributions_PCL_GBM.csv')

# Create daily balance
daily_contribution_balance_df1 = db.daily_balance(
    df=contribution_balance_df1,
    column_name='Contribuciones_GBM_MXN',
    sum=True)

# Output to CSV
file2 = 'outputs/daily_contributions_PCL_GBM.csv'
daily_contribution_balance_df1.to_csv(file2, index=True, index_label='Date')

# Output to MySQL
daily_contribution_balance_df1.to_sql(
    name='daily_contributions_PCL_GBM',  # Table name
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# CETES Account
##############################################################################
# Get contribution balance
contribution_balance_df2 = db.create_df(
    'inputs/pcl/contributions_PCL_CETES.csv')

# Create daily balance.
daily_contribution_balance_df2 = db.daily_balance(
    df=contribution_balance_df2,
    column_name='Contribuciones_Cetes_MXN',
    sum=True)

# Output to CSV
file1 = 'outputs/daily_contributions_PCL_CETES.csv'
daily_contribution_balance_df2.to_csv(file1, index=True, index_label='Date')

# Output to MySQL
daily_contribution_balance_df2.to_sql(
    name='daily_contributions_PCL_CETES',  # Table name
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# IBKR Account
##############################################################################
# Get contribution balance
contribution_balance_df3 = db.create_df(
    'inputs/pcl/contributions_PCL_IBKR.csv')

# Create daily balance.
daily_contribution_balance_df3 = db.daily_balance(
    df=contribution_balance_df3,
    column_name='Contribuciones_IBKR_MXN',
    sum=True)

# Output to CSV
file1 = 'outputs/daily_contributions_PCL_IBKR.csv'
daily_contribution_balance_df3.to_csv(file1, index=True, index_label='Date')

# Output to MySQL
daily_contribution_balance_df3.to_sql(
    name='daily_contributions_PCL_IBKR',  # Table name
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# Sum all accounts
##############################################################################
acct_1 = 'outputs/daily_contributions_PCL_GBM.csv'
acct_2 = 'outputs/daily_contributions_PCL_CETES.csv'
acct_3 = 'outputs/daily_contributions_PCL_IBKR.csv'

added_df = db.add_df(acct_1, acct_2, acct_3)
unique_df = db.remove_duplicates(added_df)
total_contributions = db.add_total_column(unique_df, 'Tot_Contribuciones_MXN')

# Output to CSV
filename4 = 'outputs/daily_contributions_PCL_AllAccounts.csv'
total_contributions.to_csv(filename4, index=False)

# Output to MySQL
total_contributions_df2 = db.create_df(filename4)

total_contributions_df2.to_sql(
    name='daily_contributions_PCL_AllAccounts',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
