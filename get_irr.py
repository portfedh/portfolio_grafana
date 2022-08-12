# Script calculates the XIRR for the investment portfolio.
# Calculation is static for the latest date available

import pandas as pd
from datetime import date
from set_engine import engine
from scripts import daily_balance as db
from scripts import irr_calculations as irr

# Create Consolidated Contributions File
########################################
file_1 = 'inputs/clg/contributions_CLG_CETES.csv'
file_2 = 'inputs/clg/contributions_CLG_GBM.csv'
total_column = 'Contribuciones_Totales_MXN'
cont_out_file = 'outputs/irr_contributions_CLG_AllAccounts.csv'

# Concatenate all files
contributions = irr.concat_df(file_1, file_2)
# Turn dataframe dates to datetime
contributions = irr.to_datetime_df(contributions, 'Date')
# Create total column
contributions = irr.add_total_df(contributions, total_column)
# Keep only Date and Total Column
contributions = irr.filter_df(contributions, [total_column])
# Invert contributions as cashflow inflows and outflows
contributions = irr.invert_cf_df(contributions, total_column)
# Turn values to integers
contributions = irr.integers_df(contributions, total_column)
# Sort values by date in ascending order
contributions.sort_index()
# Save output as CSV
contributions.to_csv(cont_out_file, index=True, index_label='Date')

# cont_file = irr.irr_contributions_df(
#     file1='inputs/clg/contributions_CLG_CETES.csv',
#     file2='inputs/clg/contributions_CLG_GBM.csv',
#     col_name1='Contribuciones_Cetes_MXN',
#     col_name2='Contribuciones_GBM_MXN',
#     sum_col_name='Tot_Contribuciones_MXN')
# cont_file.to_csv(
#     "outputs/irr_contributions_CLG_AllAccounts.csv",
#     index=True, index_label='Date')

# Create Consolidated Monthly Account Balance
#############################################
file3 = db.create_df('inputs/clg/monthly_account_balance_CLG_CETES.csv')
file4 = db.create_df('inputs/clg/monthly_account_balance_CLG_GBM.csv')
sum_col_name = 'Tot_Acct_Portafolio_MXN'
balance_out_file = 'outputs/irr_monthly_account_balance_CLG_AllAccounts.csv'

# Merge all files
balance = irr.merge_df(file3, file4)
# Create total column
balance = irr.add_total_df(balance, sum_col_name)
# Turn values to integers
balance = balance.astype('int')
# Keep only Date and Total Column
balance = irr.filter_df(balance, [sum_col_name])
# Save output as CSV
balance.to_csv(balance_out_file, index=True, index_label='Date')

# consolidated_df = irr.irr_monthly_balance_df(
#     file1=db.create_df('inputs/clg/monthly_account_balance_CLG_CETES.csv'),
#     file2=db.create_df('inputs/clg/monthly_account_balance_CLG_GBM.csv'),
#     col_name1='Tot_Acct_Cetes_MXN',
#     col_name2='Tot_Acct_GBM_MXN',
#     sum_col_name='Tot_Acct_Portafolio_MXN')
# consolidated_df.to_csv(
#     "outputs/irr_monthly_account_balance_CLG_AllAccounts.csv",
#     index=True, index_label='Date')

# Caculate IRR
##############
contrib_csv = 'outputs/irr_contributions_CLG_AllAccounts.csv'
balance_csv = 'outputs/irr_monthly_account_balance_CLG_AllAccounts.csv'
balance_df = db.create_df(balance_csv)
contributions_df = db.create_df(contrib_csv)
bal_column = 'Tot_Acct_Portafolio_MXN'
cont_column = 'Contribuciones_Totales_MXN'

# Get las value from dataframe
a = irr.get_last_value(balance_df)
# Rename column as contriburions column
b = irr.rename_column(a, bal_column, cont_column)
# Concatenate into one df
irr_df = pd.concat([contributions_df, b])
# Separate df into two lists
dates, values = irr.split_df(irr_df, cont_column)
# Pass lists into xirr function
xirr_result = irr.xirr(dates, values)

# irr_value = irr.calculate_xirr(
#     acct_balance_df=db.create_df(
#         'outputs/irr_monthly_account_balance_CLG_AllAccounts.csv'),
#     contributions_df=db.create_df(
#         'outputs/irr_contributions_CLG_AllAccounts.csv'),
#     bal_column='Tot_Acct_Portafolio_MXN',
#     cont_column='Tot_Contribuciones_MXN')

# Outputs
#########
# Save value to CSV
today = (f'{date.today():%Y-%m-%d}')
data = [today, xirr_result]
df = pd.DataFrame([data], columns=['Date', 'XIRR'])
df.to_csv("outputs/irr_xirr_CLG.csv", index=False)

# Save value to MySQL
xirr = db.create_df('outputs/irr_xirr_CLG.csv')

xirr.to_sql(
    name='irr_xirr_CLG',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
