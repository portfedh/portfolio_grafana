import pandas as pd
from datetime import date
from scripts import irr_calculations as irr
from scripts import daily_balance as dab


# Create Consolidated Contributions File
########################################
cont_file = irr.irr_contributions_df(
    'inputs/contributions_CLG_CETES.csv',
    'inputs/contributions_CLG_GBM.csv')
cont_file.to_csv("outputs/irr_contributions_CLG_AllAccounts.csv",
                 index=True, index_label='Date')

# Create Consolidated Monthly Account Balance
#############################################
balance_df = dab.create_df('inputs/monthly_account_balance_CLG_CETES.csv')
balance_df2 = dab.create_df('inputs/monthly_account_balance_CLG_GBM.csv')
consolidated_df = irr.irr_monthly_balance_df(balance_df, balance_df2)
consolidated_df.to_csv(
    "outputs/irr_monthly_account_balance_CLG_AllAccounts.csv",
    index=True, index_label='Date')

# Caculate IRR
##############

# Cambiar nombres para que no sean iguales a los de arriba
balance_df = dab.create_df('outputs/irr_monthly_account_balance_CLG_AllAccounts.csv')
balance_df2 = dab.create_df('outputs/irr_contributions_CLG_AllAccounts.csv')
irr_value = irr.calculate_xirr(balance_df, balance_df2)
# Save value to CSV
today = (f'{date.today():%Y-%m-%d}')
data = [today, irr_value]
df = pd.DataFrame([data], columns=['Date', 'XIRR'])
print(df)
df.to_csv("outputs/irr_amount.csv", index=False)
