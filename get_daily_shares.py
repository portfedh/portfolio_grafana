import set_analysis_dates as sad
from sqlalchemy import create_engine
from scripts import daily_balance as db
from scripts import daily_shares as ds

# MySQL Connection Settings
##############################################################################
url = 'mysql+pymysql://root:password1@localhost:3306/PCL_database'
engine = create_engine(url)

# Importing Trade History GBM
##############################################################################
# Get trade history
trade_hist_df = db.create_df('inputs/pcl/trade_history_PCL_GBM.csv')

# Transform Shares column from string to integer
trade_hist_df['Shares'] = trade_hist_df['Shares'].astype(int)

# Create ticker lists
yftickers = list(trade_hist_df['Yfinance_Ticker'].unique())

# Create empty share quantity dataframe
share_quantity_df = ds.create_share_quantity_df(yftickers)

# Create daily share quantity dataframe
daily_share_quantity_df = ds.create_daily_share_quantity(
    date_range=sad.date_range,
    trade_history=trade_hist_df,
    ticker_list=yftickers,
    df=share_quantity_df)

# Output to CSV
filename = 'outputs/daily_share_quantity_PCL_GBM.csv'
daily_share_quantity_df.to_csv(filename, index=True, index_label='Date')

# Output to MySQL
table_name = 'daily_share_quantity_PCL_GBM'
daily_share_quantity_df.to_sql(
    name=table_name,
    con=engine,
    if_exists='replace',
    index=True,
    index_label='Date')

# Importing Trade History IBKR
##############################################################################
# Get trade history
trade_hist_df2 = db.create_df('inputs/pcl/trade_history_PCL_IBKR.csv')

# Transform Shares column from string to integer
trade_hist_df2['Shares'] = trade_hist_df2['Shares'].astype(int)

# Create ticker lists
yftickers2 = list(trade_hist_df2['Yfinance_Ticker'].unique())

# Create empty share quantity dataframe
share_quantity_df2 = ds.create_share_quantity_df(yftickers2)

# Create daily share quantity dataframe
daily_share_quantity_df2 = ds.create_daily_share_quantity(
    date_range=sad.date_range,
    trade_history=trade_hist_df2,
    ticker_list=yftickers2,
    df=share_quantity_df2)

# Output to CSV
filename2 = 'outputs/daily_share_quantity_PCL_IBKR.csv'
daily_share_quantity_df2.to_csv(filename2, index=True, index_label='Date')

# Output to MySQL
table_name = 'daily_share_quantity_PCL_IBKR'
daily_share_quantity_df2.to_sql(
    name=table_name,
    con=engine,
    if_exists='replace',
    index=True,
    index_label='Date')
