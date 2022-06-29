import yfinance as yf
import set_analysis_dates as sad
from sqlalchemy import create_engine
from scripts import daily_balance as db

# MySQL Connection Settings
###########################
url = 'mysql+pymysql://root:password1@localhost:3306/CLG_database'
engine = create_engine(url)

# Importing Trade History GBM
#############################
# Get trade history
trade_hist_df = db.create_df('inputs/clg/trade_history_CLG_GBM.csv')

# Transform Shares column from string to integer
trade_hist_df['Shares'] = trade_hist_df['Shares'].astype(int)

# Create ticker lists
yftickers = list(trade_hist_df['Yfinance_Ticker'].unique())

# Download Yahoo finance prices
prices = yf.download(yftickers, start=sad.start_date, end=sad.end_date)

# Use closing price
closing_prices = prices.Close

# Output to CSV
filename1 = "outputs/daily_prices_original_CLG_GBM.csv"
closing_prices.to_csv(filename1, index=True, index_label='Date')

# Interpolate missing values
df_interpol = closing_prices.interpolate(
    method='linear',
    limit_direction='both')
df_interpol.tail(10)

# Outputs
#########
# Output to CSV
filename2 = 'outputs/daily_prices_interpolated_CLG_GBM.csv'
df_interpol.to_csv(filename2, index=True, index_label='Date')

# Output to MySQL
table_name = 'daily_prices_CLG_GBM'
closing_prices.to_sql(
    name=table_name,
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
