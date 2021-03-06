import pandas as pd
from datetime import date
from sqlalchemy import create_engine
from scripts import daily_balance as db
from scripts import irr_calculations as irr


# MySQL Connection Settings
###########################
url = 'mysql+pymysql://root:password1@localhost:3306/CLG_database'
engine = create_engine(url)

# Create Consolidated Contributions File
########################################
cont_file = irr.irr_contributions_df(
    file1='inputs/clg/contributions_CLG_CETES.csv',
    file2='inputs/clg/contributions_CLG_GBM.csv',
    col_name1='Contribuciones_Cetes_MXN',
    col_name2='Contribuciones_GBM_MXN',
    sum_col_name='Tot_Contribuciones_MXN')
cont_file.to_csv(
    "outputs/irr_contributions_CLG_AllAccounts.csv",
    index=True, index_label='Date')

# Create Consolidated Monthly Account Balance
#############################################
consolidated_df = irr.irr_monthly_balance_df(
    file1=db.create_df('inputs/clg/monthly_account_balance_CLG_CETES.csv'),
    file2=db.create_df('inputs/clg/monthly_account_balance_CLG_GBM.csv'),
    col_name1='Tot_Acct_Cetes_MXN',
    col_name2='Tot_Acct_GBM_MXN',
    sum_col_name='Tot_Acct_Portafolio_MXN')

# Save value to CSV
consolidated_df.to_csv(
    "outputs/irr_monthly_account_balance_CLG_AllAccounts.csv",
    index=True, index_label='Date')

# Caculate IRR
##############
irr_value = irr.calculate_xirr(
    acct_balance_df=db.create_df(
        'outputs/irr_monthly_account_balance_CLG_AllAccounts.csv'),
    contributions_df=db.create_df(
        'outputs/irr_contributions_CLG_AllAccounts.csv'),
    bal_column='Tot_Acct_Portafolio_MXN',
    cont_column='Tot_Contribuciones_MXN')

# Outputs
#########
# Save value to CSV
today = (f'{date.today():%Y-%m-%d}')
data = [today, irr_value]
df = pd.DataFrame([data], columns=['Date', 'XIRR'])
df.to_csv("outputs/irr_xirr_CLG.csv", index=False)

# Save value to MySQL
xirr = db.create_df('outputs/irr_xirr_CLG.csv')

xirr.to_sql(
    name='irr_xirr_CLG',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
