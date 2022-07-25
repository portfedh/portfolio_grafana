import pandas as pd
from datetime import date
from sqlalchemy import create_engine
from scripts import daily_balance as db
from scripts import irr_calculations as irr


# MySQL Connection Settings
###########################
url = 'mysql+pymysql://root:password1@localhost:3306/PCL_database'
engine = create_engine(url)

# Create Consolidated Contributions File: V2
############################################
file_1 = 'inputs/pcl/contributions_PCL_CETES.csv'
file_2 = 'inputs/pcl/contributions_PCL_GBM.csv'
file_3 = 'inputs/pcl/contributions_PCL_IBKR.csv'
total_column = 'Contribuciones_Totales_MXN'
cont_out_file = "outputs/irr_contributions_PCL_AllAccounts.csv"

# Concatenate all files
contributions = irr.concat_df(file_1, file_2, file_3)
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

"""
# Create Consolidated Contributions File
########################################
cont_file = irr.irr_contributions_df(
    file1='inputs/pcl/contributions_PCL_CETES.csv',
    file2='inputs/pcl/contributions_PCL_GBM.csv',
    col_name1='Contribuciones_Cetes_MXN',
    col_name2='Contribuciones_GBM_MXN',
    sum_col_name='Tot_Contribuciones_MXN')
cont_file.to_csv(
    "outputs/irr_contributions_PCL_AllAccounts.csv",
    index=True, index_label='Date')
"""

# Create Consolidated Monthly Account Balance
#############################################
consolidated_df = irr.irr_monthly_balance_df(
    file1=db.create_df('inputs/pcl/monthly_account_balance_PCL_CETES.csv'),
    file2=db.create_df('inputs/pcl/monthly_account_balance_PCL_GBM.csv'),
    col_name1='Tot_Acct_Cetes_MXN',
    col_name2='Tot_Acct_GBM_MXN',
    sum_col_name='Tot_Acct_Portafolio_MXN')

# Save value to CSV
consolidated_df.to_csv(
    "outputs/irr_monthly_account_balance_PCL_AllAccounts.csv",
    index=True, index_label='Date')

# Caculate IRR
##############
irr_value = irr.calculate_xirr(
    acct_balance_df=db.create_df(
        'outputs/irr_monthly_account_balance_PCL_AllAccounts.csv'),
    contributions_df=db.create_df(
        'outputs/irr_contributions_PCL_AllAccounts.csv'),
    bal_column='Tot_Acct_Portafolio_MXN',
    cont_column='Tot_Contribuciones_MXN')

# Outputs
#########
# Save value to CSV
today = (f'{date.today():%Y-%m-%d}')
data = [today, irr_value]
df = pd.DataFrame([data], columns=['Date', 'XIRR'])
df.to_csv("outputs/irr_xirr_PCL.csv", index=False)

# Save value to MySQL
xirr = db.create_df('outputs/irr_xirr_PCL.csv')

xirr.to_sql(
    name='irr_xirr_PCL',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
