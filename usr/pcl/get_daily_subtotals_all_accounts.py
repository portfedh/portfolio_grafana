# Script creates subtotal amounts for asset allocations

import pandas as pd
from set_engine import engine
import move_two_levels_up
from scripts import daily_balance as db

# Imports
#########
# Import CSV files and create data frames
gbm_df = db.create_df('outputs/daily_subtotals_PCL_GBM.csv')
ibkr_df = db.create_df('outputs/daily_subtotals_PCL_IBKR.csv')
cetes_df = db.create_df('outputs/daily_acct_balance_PCL_CETES.csv')

# Portfolio Calculations
########################
# Create Subtotals DataFrame ($)
subtotals = pd.DataFrame()
subtotals.index.name = 'Date'

# Total Fixed Income GBM ($)
subtotals['Tot_FixedIncome_GBM'] = (
    gbm_df['Sub_BNDX'] +
    gbm_df['Sub_BND'] +
    gbm_df['Sub_SHV'])

# Total Fixed Income GBM + CETES ($)
subtotals['Tot_FixedIncome'] = (
    gbm_df['Sub_BNDX'] +
    gbm_df['Sub_BND'] +
    gbm_df['Sub_SHV'] +
    cetes_df['Tot_Acct_Cetes_MXN'])

# Total Equity GBM + IBKR($)
subtotals['Tot_Equity'] = (
    gbm_df['Sub_VGK'] +
    gbm_df['Sub_IEMG'] +
    gbm_df['Sub_VTI'] +
    gbm_df['Sub_VPL'] +
    gbm_df['Sub_VOO'] +
    gbm_df['Sub_MCHI'] +
    gbm_df['Sub_BABAN'] +
    gbm_df['Sub_PG'] +
    gbm_df['Sub_INTC'] +
    ibkr_df['Sub_VPL'] +
    ibkr_df['Sub_IEMG'] +
    ibkr_df['Sub_BABAN'] +
    ibkr_df['Sub_PG'])

# Total Alternatives GBM ($)
subtotals['Tot_Alternatives'] = (
    gbm_df['Sub_GOLDN'] +
    gbm_df['Sub_FIBRAPL14'])

# Total  Portafolio ($)
subtotals['Tot_Portfolio'] = (
    subtotals['Tot_Equity'] +
    subtotals['Tot_FixedIncome'] +
    subtotals['Tot_Alternatives'])

# Outputs
#########

# Output to CSV
filename = 'outputs/daily_subtotals_PCL_AllAccounts.csv'
subtotals.to_csv(filename, index=True, index_label='Date')

# Output to MySQL
table_name = 'daily_subtotals_PCL_AllAccounts'
subtotals.to_sql(name=table_name, con=engine, if_exists='replace',
                 index=True, index_label='Date')
