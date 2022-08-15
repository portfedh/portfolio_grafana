# Script to create subtotal amounts from price & quantity data per account

import pandas as pd
from set_engine import engine
from scripts import daily_balance as db

# GBM Account
##############################################################################

# Imports
#########
# Import CSV files and create data frames
shares_gbm_df = db.create_df('outputs/daily_share_quantity_CLG_GBM.csv')
prices_gbm_df = db.create_df('outputs/daily_prices_interpolated_CLG_GBM.csv')
cetes_df = db.create_df('outputs/daily_acct_balance_CLG_CETES.csv')

# Transformations
#################
# Rename columns: Add quantity or price symbol
shares_df = shares_gbm_df.add_prefix('Q_')
prices_df = prices_gbm_df.add_prefix('P_')
# Rename columns: Remove .MX to avoid problems in SQL
shares_df.columns = shares_df.columns.str.removesuffix('.MX')
prices_df.columns = prices_df.columns.str.removesuffix('.MX')
# Merge Dataframes
new_df = pd.concat(([shares_df, prices_df, cetes_df]), axis=1)
# Interpolate missing values (prices are NaN on weekend dates)
interpol_gbm_df = new_df.interpolate(
    method='linear', limit_direction='both')

# Subtotal Calculations
########################
# Tickers and column drop are hardcoded
# Subtotals ($)
tickers_gbm = ['VOO', 'VGK', 'VPL', 'IEMG', 'MCHI', 'GOLDN', 'FIBRAPL14',
               'CETETRCISHRS', 'IB1MXXN', 'SHV', 'BABAN', 'PG', 'META', 'INTC',
               'BAC', 'MU']
for x in tickers_gbm:
    interpol_gbm_df[f'Sub_{x}'] = (
        interpol_gbm_df[f'Q_{x}'] *
        interpol_gbm_df[f'P_{x}'])
# Reorder Column Position
# Check every time new tickers are added.
my_column = interpol_gbm_df.pop('Tot_Acct_Cetes_MXN')
interpol_gbm_df.insert(31, my_column.name, my_column)
# Remove Quantity and Price Columns
# Check every time new tickers are added.
interpol_gbm_df.drop(interpol_gbm_df.iloc[:, 0:20], inplace=True, axis=1)

# Outputs
#########
# Output to CSV
filename = 'outputs/daily_subtotals_CLG_GBM.csv'
interpol_gbm_df.to_csv(filename, index=True, index_label='Date')

# Output to MySQL
table_name = 'daily_subtotals_CLG_GBM'
interpol_gbm_df.to_sql(name=table_name, con=engine, if_exists='replace',
                       index=True, index_label='Date')
