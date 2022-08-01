import yfinance as yf
import set_analysis_dates as sad
from sqlalchemy import create_engine
from scripts import daily_balance as db

# MySQL Connection Settings
###########################
url = 'mysql+pymysql://root:password1@localhost:3306/PCL_database'
engine = create_engine(url)

# Importing Trade History GBM
##############################################################################
# Get trade history
trade_hist_df = db.create_df('inputs/pcl/trade_history_PCL_GBM.csv')

# Create ticker lists
yftickers = list(trade_hist_df['Yfinance_Ticker'].unique())

# Download Yahoo finance prices
prices_df = yf.download(yftickers, start=sad.start_date, end=sad.end_date)

# Use closing price
prices_df = prices_df.Close

# Output to CSV
filename1 = "outputs/daily_prices_original_PCL_GBM.csv"
prices_df.to_csv(filename1, index=True, index_label='Date')

# Interpolate missing values
df_interpol = prices_df.interpolate(
    method='linear',
    limit_direction='both')

# Output to CSV
filename2 = 'outputs/daily_prices_interpolated_PCL_GBM.csv'
df_interpol.to_csv(filename2, index=True, index_label='Date')

# Output to MySQL
prices_df.columns = (prices_df.columns.str.replace('.', '_', regex=False))
table_name = 'daily_prices_PCL_GBM'
prices_df.to_sql(
    name=table_name,
    con=engine,
    if_exists='replace',
    index=True,
    index_label='Date')

# Importing Trade History IBKR
##############################################################################