# Script to calculate the daily balance of the portfolio
# for every day within the investment period.


from set_engine import engine
import move_two_levels_up
from scripts import daily_balance as db
from set_analysis_dates import date_range


# GBM Account
##############################################################################
# Get monthly balance
balance_df1 = db.create_df('inputs/clg/monthly_account_balance_CLG_GBM.csv')

# Create daily balance
daily_balance_df1 = db.create_daily_balance_df(
    df=balance_df1,
    column_name='Tot_Acct_GBM_MXN',
    sum=False,
    range=date_range)

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
daily_balance_df2 = db.create_daily_balance_df(
    df=balance_df2,
    column_name='Tot_Acct_Cetes_MXN',
    sum=False,
    range=date_range)

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
acct_1 = db.create_df('outputs/daily_acct_balance_CLG_CETES.csv')
acct_2 = db.create_df('outputs/daily_acct_balance_CLG_GBM.csv')

added_df = db.concat_df(acct_1, acct_2, type=1)
total_balance_df = db.add_total_column_to_df(added_df, 'Tot_Acct_Portafolio_MXN')

# Output to CSV
filename3 = 'outputs/daily_acct_balance_CLG_AllAccounts.csv'
total_balance_df.to_csv(filename3, index=True, index_label='Date')

# Output to MySQL
total_balance_df2 = db.create_df(filename3)

total_balance_df2.to_sql(
    name='daily_acct_balance_CLG_AllAccounts',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
