# Script creates subtotal amounts for asset allocations

import pandas as pd
from set_engine import engine
import move_two_levels_up
from scripts import daily_balance as db

# Imports
#########
# Import CSV files and create data frames
account1_df = db.create_df('outputs/daily_subtotals_user1_account1.csv')
account2_df = db.create_df('outputs/daily_subtotals_user1_account2.csv')

# Portfolio Calculations
########################
# Create Subtotals DataFrame ($)
subtotals = pd.DataFrame()
subtotals.index.name = 'Date'

# Total Fixed Income ($)
subtotals['Tot_FixedIncome'] = (
    account1_df['Sub_BNDX'] +
    account1_df['Sub_BND'] +
    account2_df['Sub_BNDX'] +
    account2_df['Sub_BND']
    )

# Total Equity ($)
subtotals['Tot_Equity'] = (
    account1_df['Sub_VTI'] +
    account1_df['Sub_VXUS'] +
    account2_df['Sub_VOO'] +
    account2_df['Sub_VEA'] +
    account2_df['Sub_VWO'])

# Total  Portafolio ($)
subtotals['Tot_Portfolio'] = (
    subtotals['Tot_Equity'] +
    subtotals['Tot_FixedIncome'])

# Outputs
#########

# Output to CSV
filename = 'outputs/daily_subtotals_user1_AllAccounts.csv'
subtotals.to_csv(filename, index=True, index_label='Date')

# Output to MySQL
table_name = 'daily_subtotals_user1_AllAccounts'
subtotals.to_sql(name=table_name, con=engine, if_exists='replace',
                 index=True, index_label='Date')
