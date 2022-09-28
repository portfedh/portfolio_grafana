# Script to get daily share quantities for every ticker in the portfolio

from set_engine import engine
import set_analysis_dates as sad
import move_two_levels_up
from scripts import daily_balance as db
from scripts import daily_shares as ds

# Importing Trade History Account1
##################################
# Get trade history
trade_hist_df = db.create_df('inputs/user1/trade_history_user1_account1.csv')

# Transform shares column from string to integer
trade_hist_df['Shares'] = trade_hist_df['Shares'].astype(int)

# Create ticker lists
yftickers = list(trade_hist_df['Yfinance_Ticker'].unique())

# Create empty share quantity DataFrame
share_quantity_df = ds.create_empty_share_quantity_df(yftickers)

# Create daily share quantity DataFrame
daily_share_quantity_df = ds.create_daily_share_quantity_df(
    date_range=sad.date_range,
    trade_history=trade_hist_df,
    ticker_list=yftickers,
    df=share_quantity_df)

# Output to CSV
filename = 'outputs/daily_share_quantity_user1_account1.csv'
daily_share_quantity_df.to_csv(filename, index=True, index_label='Date')

# Output to MySQL
daily_share_quantity_df.to_sql(
    name='daily_share_quantity_user1_account1',
    con=engine,
    if_exists='replace',
    index=True,
    index_label='Date')


# Importing Trade History Account2
##################################
# Get trade history
trade_hist_df = db.create_df('inputs/user1/trade_history_user1_account2.csv')

# Transform shares column from string to integer
trade_hist_df['Shares'] = trade_hist_df['Shares'].astype(int)

# Create ticker lists
yftickers = list(trade_hist_df['Yfinance_Ticker'].unique())

# Create empty share quantity DataFrame
share_quantity_df = ds.create_empty_share_quantity_df(yftickers)

# Create daily share quantity DataFrame
daily_share_quantity_df = ds.create_daily_share_quantity_df(
    date_range=sad.date_range,
    trade_history=trade_hist_df,
    ticker_list=yftickers,
    df=share_quantity_df)

# Output to CSV
filename = 'outputs/daily_share_quantity_user1_account2.csv'
daily_share_quantity_df.to_csv(filename, index=True, index_label='Date')

# Output to MySQL
daily_share_quantity_df.to_sql(
    name='daily_share_quantity_user1_account2',
    con=engine,
    if_exists='replace',
    index=True,
    index_label='Date')
