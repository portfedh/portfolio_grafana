import yfinance as yf
import set_analysis_dates as sad
from sqlalchemy import create_engine
from scripts import daily_balance as db

# MySQL Connection Settings
###########################
engine = create_engine(
    'mysql+pymysql://root:password1@localhost:3306/CLG_database')

# Importing Trade History GBM
#############################
# Get trade history
trade_hist_df = db.create_df('inputs/trade_history_CLG_GBM.csv')

# Transform Shares column from string to integer
trade_hist_df['Shares'] = trade_hist_df['Shares'].astype(int)

# Create ticker lists
yftickers = list(trade_hist_df['Yfinance_Ticker'].unique())

# Download Yahoo finance prices
prices = yf.download(yftickers, start=sad.start_date, end=sad.end_date)

# Use closing price
closing_prices = prices.Close

# Output to CSV
closing_prices.to_csv(
    "outputs/daily_prices_original_CLG_GBM.csv",
    index=True, index_label='Date')

# Interpolate missing values
df_interpol = closing_prices.interpolate(
    method='linear',
    limit_direction='both')
df_interpol.tail(10)

# Outputs
#########
# Output to CSV
df_interpol.to_csv(
    "outputs/daily_prices_interpolated_CLG_GBM.csv",
    index=True, index_label='Date')

# Output to MySQL
closing_prices.to_sql(
    name='daily_prices_CLG_GBM',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
