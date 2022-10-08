# Script to calculate the daily balance of the portfolio
# for every day within the investment period.


from set_engine import engine
import move_two_levels_up
from scripts import daily_balance as db
from set_analysis_dates import date_range


# Account 1
###########
# Get monthly balance
balance_path1 = 'inputs/user1/monthly_account_balance_user1_account1.csv'
balance_df1 = db.create_df(balance_path1)

# Create daily balance
daily_balance_df1 = db.create_daily_balance_df(
    df=balance_df1,
    column_name='Tot_Acct_Bank1_USD',
    sum=False,
    range=date_range)

# Output to CSV
filename1 = 'outputs/daily_acct_balance_user1_account1.csv'
daily_balance_df1.to_csv(filename1, index=True, index_label='Date')

# Output to MySQL
daily_balance_df1.to_sql(
    name='daily_acct_balance_user1_account1',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# Account 2
###########
# Get monthly balance
balance_path2 = 'inputs/user1/monthly_account_balance_user1_account2.csv'
balance_df2 = db.create_df(balance_path2)

# Create daily balance
daily_balance_df2 = db.create_daily_balance_df(
    df=balance_df2,
    column_name='Tot_Acct_Bank2_USD',
    sum=False,
    range=date_range)

# Output to CSV
filename2 = 'outputs/daily_acct_balance_user1_account2.csv'
daily_balance_df2.to_csv(filename2, index=True, index_label='Date')

# Output to MySQL
daily_balance_df2.to_sql(
    name='daily_acct_balance_user1_account2',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# Sum All Accounts
##################
acct_1 = db.create_df('outputs/daily_acct_balance_user1_account1.csv')
acct_2 = db.create_df('outputs/daily_acct_balance_user1_account2.csv')

added_df = db.concat_df(acct_1, acct_2, type=1)
total_balance_df = db.add_total_column_to_df(
    added_df, 'Tot_Acct_Portfolio_USD')

# Output to CSV
filename3 = 'outputs/daily_acct_balance_user1_AllAccounts.csv'
total_balance_df.to_csv(filename3, index=True, index_label='Date')

# Output to MySQL
total_balance_df2 = db.create_df(filename3)

total_balance_df2.to_sql(
    name='daily_acct_balance_user1_AllAccounts',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
