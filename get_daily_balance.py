import daily_balance

# GBM Account
#############
# Get monthly balance
balance_df = daily_balance.create_balance_df('Inputs/CLG_GBM_Balances.csv')
# Create daily balance
daily_balance_df = daily_balance.create_daily_balance_df(balance_df, 'Tot_Cta_GBM_MXN')
# Output to CSV
daily_balance_df.to_csv("Outputs/balance_gbm_diario.csv", index=True, index_label='Date')

# CETES Account
###############
# Get monthly balance
balance_df2 = daily_balance.create_balance_df('Inputs/CLG_CETES_Balances.csv')
# Create daily balance
daily_balance_df2 = daily_balance.create_daily_balance_df(balance_df2, 'Tot_Cta_Cetes_MXN')
# Output to CSV
daily_balance_df2.to_csv("Outputs/balance_cetes_diario.csv", index=True, index_label='Date')