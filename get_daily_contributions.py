from scripts import daily_contribution_balance

# CETES Account
#############
# Get contribution balance
contribution_balance_df = daily_contribution_balance.contribution_balance_df('inputs/contributions_CLG_CETES.csv')
# Create daily balance.
daily_contribution_balance_df = daily_contribution_balance.daily_contribution_balance_df(contribution_balance_df, 'Contribuciones_Cetes_MXN')
# Output to CSV
daily_contribution_balance_df.to_csv("outputs/daily_contributions_CLG_CETES.csv", index=True, index_label='Date')

# GBM Account
###############
# Get monthly balance
contribution_balance_df2 = daily_contribution_balance.contribution_balance_df('inputs/contributions_CLG_GBM.csv')
# Create daily balance
daily_contribution_balance_df2 = daily_contribution_balance.daily_contribution_balance_df(contribution_balance_df2, 'Contribuciones_GBM_MXN')
# Output to CSV
daily_contribution_balance_df2.to_csv("outputs/daily_contributions_CLG_GBM.csv", index=True, index_label='Date')

# Sum both Accounts
###################
"""
# Accounts
cetes_contributions = 'outputs/daily_contributions_CLG_CETES.csv'
gbm_contributions = 'outputs/daily_contributions_CLG_GBM.csv'
# Get total daily balance
total_contributions_df = daily_contribution_balance.sum_total_daily_contribution_balance_df(cetes_acct, gbm_acct)
# Output to CSV
total_contributions_df.to_csv("outputs/balance_total_diario.csv", index=False)
"""