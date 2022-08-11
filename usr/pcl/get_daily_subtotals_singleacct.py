# Script to create subtotal amounts from price & quantity data per account

import pandas as pd
from set_engine import engine
from scripts import daily_balance as db

# GBM Account
##############################################################################

# Imports
#########
# Import CSV files and create data frames
shares_gbm_df = db.create_df('outputs/daily_share_quantity_PCL_GBM.csv')
prices_gbm_df = db.create_df('outputs/daily_prices_interpolated_PCL_GBM.csv')

# Transformations
#################
# Rename columns: Add Quantity or price simbol
shares_gbm_df = shares_gbm_df.add_prefix('Q_')
prices_gbm_df = prices_gbm_df.add_prefix('P_')
# Rename columns: Remove .MX to avoid problems in SQL
shares_gbm_df.columns = shares_gbm_df.columns.str.removesuffix('.MX')
prices_gbm_df.columns = prices_gbm_df.columns.str.removesuffix('.MX')
# Merge Dataframes
concat_gbm_df = pd.concat(([shares_gbm_df, prices_gbm_df]), axis=1)
# Interpolate missing values (prices are NaN on weekend dates)
interpol_gbm_df = concat_gbm_df.interpolate(
    method='linear', limit_direction='both')

# Subtotal Calculations
########################
# Tickers and column drop are hardcoded
# Subtotals ($)
tickers_gbm = ['VGK', 'IEMG', 'VTI', 'BNDX', 'BND', 'VPL', 'VOO', 'SHV',
               'MCHI', 'GOLDN', 'FIBRAPL14', 'BABAN', 'PG', 'INTC']
# Calculate subtotals
for x in tickers_gbm:
    interpol_gbm_df[f'Sub_{x}'] = (
        interpol_gbm_df[f'Q_{x}'] *
        interpol_gbm_df[f'P_{x}'])
# Remove Quantity and Price Columns
# Re-check if new tickers are added.
interpol_gbm_df.drop(interpol_gbm_df.iloc[:, 0:28], inplace=True, axis=1)

# Outputs
##########
# Output to CSV
filename1 = 'outputs/daily_subtotals_PCL_GBM.csv'
interpol_gbm_df.to_csv(filename1, index=True, index_label='Date')

# Output to MySQL
table_name1 = 'daily_subtotals_PCL_GBM'
interpol_gbm_df.to_sql(name=table_name1, con=engine, if_exists='replace',
                       index=True, index_label='Date')

# IBKR Account
##############################################################################

# Imports
#########
# Import CSV files and create data frames
shares_ibkr_df = db.create_df('outputs/daily_share_quantity_PCL_IBKR.csv')
prices_ibkr_df = db.create_df('outputs/daily_prices_interpolated_PCL_IBKR.csv')

# Transformations
#################
# Rename columns: Add Quantity or price simbol
shares_ibkr_df = shares_ibkr_df.add_prefix('Q_')
prices_ibkr_df = prices_ibkr_df.add_prefix('P_')

# Rename columns: Remove .MX to avoid problems in SQL
shares_ibkr_df.columns = shares_ibkr_df.columns.str.removesuffix('.MX')
prices_ibkr_df.columns = prices_ibkr_df.columns.str.removesuffix('.MX')

# Merge Dataframes
concat_df_ibkr = pd.concat(([shares_ibkr_df, prices_ibkr_df]), axis=1)
# Interpolate missing values (prices are NaN on weekend dates)
interpol_ibkr_df = concat_df_ibkr.interpolate(
    method='linear', limit_direction='both')

# Portfolio Calculations
########################
# Tickers and column drop are hardcoded
# Subtotals ($)
tickers_ibkr = ['VPL', 'IEMG', 'BABAN', 'PG']
# Calculate subtotals
for x in tickers_ibkr:
    interpol_ibkr_df[f'Sub_{x}'] = (
        interpol_ibkr_df[f'Q_{x}'] *
        interpol_ibkr_df[f'P_{x}'])
# Remove Quantity and Price Columns
interpol_ibkr_df.drop(interpol_ibkr_df.iloc[:, 0:8], inplace=True, axis=1)

# Outputs
#########
# Output to CSV
filename2 = 'outputs/daily_subtotals_PCL_IBKR.csv'
interpol_ibkr_df.to_csv(filename2, index=True, index_label='Date')

# # Output to MySQL
table_name2 = 'daily_subtotals_PCL_IBKR'
interpol_ibkr_df.to_sql(name=table_name2, con=engine, if_exists='replace',
                        index=True, index_label='Date')
