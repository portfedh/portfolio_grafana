import set_analysis_dates as sad
from sqlalchemy import create_engine
from scripts import daily_balance as db
from scripts import daily_shares as ds

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
tickers = list(trade_hist_df['Ticker'].unique())

# Create empty share quantity dataframe
share_quantity_df = ds.create_share_quantity_df(yftickers)

# Create daily share quantity dataframe
daily_share_quantity_df = ds.create_daily_share_quantity(
    date_range=sad.date_range,
    df=trade_hist_df,
    ticker_list=yftickers,
    shares=share_quantity_df)

# Output to CSV
daily_share_quantity_df.to_csv(
    "outputs/daily_share_quantity_CLG_GBM.csv",
    index=True, index_label='Date')

# Output to MySQL
daily_share_quantity_df.to_sql(
    name='daily_share_quantity_CLG_GBM',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
