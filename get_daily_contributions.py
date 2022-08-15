# Script to get the accumulated net contributions
# for every day during the investment period.

from set_engine import engine
from scripts import daily_balance as db

# GBM Account
##############################################################################
# Get monthly balance
contribution_balance_df1 = db.create_df(
    'inputs/clg/contributions_CLG_GBM.csv')

# Create daily balance
daily_contribution_balance_df1 = db.daily_balance(
    df=contribution_balance_df1,
    column_name='Contribuciones_GBM_MXN',
    sum=True)

# Output to CSV
file1 = 'outputs/daily_contributions_CLG_GBM.csv'
daily_contribution_balance_df1.to_csv(file1, index=True, index_label='Date')

# Output to MySQL
daily_contribution_balance_df1.to_sql(
    name='daily_contributions_CLG_GBM',  # Table name
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')


# CETES Account
##############################################################################
# Get contribution balance
contribution_balance_df2 = db.create_df(
    'inputs/clg/contributions_CLG_CETES.csv')

# Create daily balance.
daily_contribution_balance_df2 = db.daily_balance(
    df=contribution_balance_df2,
    column_name='Contribuciones_Cetes_MXN',
    sum=True)

# Output to CSV
file2 = 'outputs/daily_contributions_CLG_CETES.csv'
daily_contribution_balance_df2.to_csv(file2, index=True, index_label='Date')

# Output to MySQL
daily_contribution_balance_df2.to_sql(
    name='daily_contributions_CLG_CETES',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')


# Sum all accounts
##############################################################################
acct_1 = 'outputs/daily_contributions_CLG_GBM.csv'
acct_2 = 'outputs/daily_contributions_CLG_CETES.csv'

added_df = db.add_df(acct_1, acct_2)
unique_df = db.remove_duplicates(added_df)
total_contributions = db.add_total_column(unique_df, 'Tot_Contribuciones_MXN')

# Output to CSV
file3 = 'outputs/daily_contributions_CLG_AllAccounts.csv'
total_contributions.to_csv(file3, index=False)

# Output to MySQL
total_contributions_df2 = db.create_df(file3)

total_contributions_df2.to_sql(
    name='daily_contributions_CLG_AllAccounts',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
