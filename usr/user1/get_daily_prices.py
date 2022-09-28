# Script to get daily prices for every ticker in the portfolio.


import yfinance as yf
from set_engine import engine
import set_analysis_dates as sad
import move_two_levels_up
from scripts import daily_balance as db


# Importing Trade History Account 1
###################################
# Get trade history
trade_hist_df = db.create_df('inputs/user1/trade_history_user1_account1.csv')

# Create ticker lists
yftickers = list(trade_hist_df['Yfinance_Ticker'].unique())

# Download Yahoo finance prices
prices_df = yf.download(yftickers, start=sad.start_date, end=sad.end_date)

# Use closing price
prices_df = prices_df.Close

# Output to CSV
filename1 = "outputs/daily_prices_original_user1_account1.csv"
prices_df.to_csv(filename1, index=True, index_label='Date')

# Interpolate missing values
df_interpol = prices_df.interpolate(
    method='linear',
    limit_direction='both')

# Output to CSV
filename2 = 'outputs/daily_prices_interpolated_user1_account1.csv'
df_interpol.to_csv(filename2, index=True, index_label='Date')

# Output to MySQL
prices_df.columns = (prices_df.columns.str.replace('.', '_', regex=False))
table_name = 'daily_prices_user1_account1'
prices_df.to_sql(
    name=table_name,
    con=engine,
    if_exists='replace',
    index=True,
    index_label='Date')


# Importing Trade History Account 2
###################################
# Get trade history
trade_hist_df = db.create_df('inputs/user1/trade_history_user1_account2.csv')

# Create ticker lists
yftickers = list(trade_hist_df['Yfinance_Ticker'].unique())

# Download Yahoo finance prices
prices_df = yf.download(yftickers, start=sad.start_date, end=sad.end_date)

# Use closing price
prices_df = prices_df.Close

# Output to CSV
filename1 = "outputs/daily_prices_original_user1_account2.csv"
prices_df.to_csv(filename1, index=True, index_label='Date')

# Interpolate missing values
df_interpol = prices_df.interpolate(
    method='linear',
    limit_direction='both')

# Output to CSV
filename2 = 'outputs/daily_prices_interpolated_user1_account2.csv'
df_interpol.to_csv(filename2, index=True, index_label='Date')

# Output to MySQL
prices_df.columns = (prices_df.columns.str.replace('.', '_', regex=False))
table_name = 'daily_prices_user1_account2'
prices_df.to_sql(
    name=table_name,
    con=engine,
    if_exists='replace',
    index=True,
    index_label='Date')
