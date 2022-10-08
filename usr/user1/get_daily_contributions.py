# Script to get the accumulated net contributions
# for every day during the investment period.


from set_engine import engine
import move_two_levels_up
from scripts import daily_balance as db
from set_analysis_dates import date_range


# Account 1
###########
# Get monthly balance
contribution_balance_df1 = db.create_df(
    'inputs/user1/contributions_user1_account1.csv')

# Create daily balance
daily_contribution_balance_df1 = db.create_daily_balance_df(
    df=contribution_balance_df1,
    column_name='Contributions_Account1_USD',
    sum=True,
    range=date_range)

# Output to CSV
file1 = 'outputs/daily_contributions_user1_account1.csv'
daily_contribution_balance_df1.to_csv(file1, index=True, index_label='Date')

# Output to MySQL
daily_contribution_balance_df1.to_sql(
    name='daily_contributions_user1_account1',  # Table name
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')


# Account 2
###########
# Get contribution balance
contribution_balance_df2 = db.create_df(
    'inputs/user1/contributions_user1_account2.csv')

# Create daily balance.
daily_contribution_balance_df2 = db.create_daily_balance_df(
    df=contribution_balance_df2,
    column_name='Contributions_Account2_USD',
    sum=True,
    range=date_range)

# Output to CSV
file2 = 'outputs/daily_contributions_user1_account2.csv'
daily_contribution_balance_df2.to_csv(file2, index=True, index_label='Date')

# Output to MySQL
daily_contribution_balance_df2.to_sql(
    name='daily_contributions_user1_account2',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')


# Sum all accounts
##################
acct_1 = db.create_df('outputs/daily_contributions_user1_account1.csv')
acct_2 = db.create_df('outputs/daily_contributions_user1_account2.csv')

added_df = db.concat_df(acct_1, acct_2, type=1)
total_contributions = db.add_total_column_to_df(
    added_df, 'Tot_Contributions_USD')

# Output to CSV
file3 = 'outputs/daily_contributions_user1_AllAccounts.csv'
total_contributions.to_csv(file3, index=True, index_label='Date')

# Output to MySQL
total_contributions_df2 = db.create_df(file3)

total_contributions_df2.to_sql(
    name='daily_contributions_user1_AllAccounts',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
