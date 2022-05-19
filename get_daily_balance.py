from scripts import daily_account_balance as dab

# CETES Account
###############
# Get monthly balance
balance_df2 = dab.create_balance_df('inputs/monthly_account_balance_CLG_CETES.csv')
# Create daily balance
daily_balance_df2 = dab.create_daily_balance_df(balance_df2, 'Tot_Acct_Cetes_MXN')
# Output to CSV
daily_balance_df2.to_csv("outputs/daily_acct_balance_CLG_CETES.csv", index=True, index_label='Date')

# GBM Account
#############
# Get monthly balance
balance_df = dab.create_balance_df('inputs/monthly_account_balance_CLG_GBM.csv')
# Create daily balance
daily_balance_df = dab.create_daily_balance_df(balance_df, 'Tot_Acct_GBM_MXN')
# Output to CSV
daily_balance_df.to_csv("outputs/daily_acct_balance_CLG_GBM.csv", index=True, index_label='Date')

# Sum both Accounts
###################
# Accounts
cetes_acct = 'outputs/daily_acct_balance_CLG_CETES.csv'
gbm_acct = 'outputs/daily_acct_balance_CLG_GBM.csv'
# Get total daily balance
total_balance_df = dab.sum_daily_balance_df(cetes_acct, gbm_acct)
# Output to CSV
total_balance_df.to_csv("outputs/daily_acct_balance_CLG_AllAccounts.csv", index=False)