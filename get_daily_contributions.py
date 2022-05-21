from scripts import daily_contribution_balance as dcb

# CETES Account
#############
# Get contribution balance
contribution_balance_df = dcb.create_contribution_df(
    'inputs/contributions_CLG_CETES.csv')
# Create daily balance.
daily_contribution_balance_df = dcb.create_daily_contribution_df(
    contribution_balance_df, 'Contribuciones_Cetes_MXN')
# Output to CSV
daily_contribution_balance_df.to_csv(
    "outputs/daily_contributions_CLG_CETES.csv",
    index=True, index_label='Date')

# GBM Account
###############
# Get monthly balance
contribution_balance_df2 = dcb.create_contribution_df(
    'inputs/contributions_CLG_GBM.csv')
# Create daily balance
daily_contribution_balance_df2 = dcb.create_daily_contribution_df(
    contribution_balance_df2, 'Contribuciones_GBM_MXN')
# Output to CSV
daily_contribution_balance_df2.to_csv(
    "outputs/daily_contributions_CLG_GBM.csv", index=True, index_label='Date')

# Sum both Accounts
###################
# Accounts
cetes_contributions = 'outputs/daily_contributions_CLG_CETES.csv'
gbm_contributions = 'outputs/daily_contributions_CLG_GBM.csv'
# Get total daily balance
total_contributions_df = dcb.sum_daily_contribution_df(cetes_contributions,
                                                       gbm_contributions)
# Output to CSV
total_contributions_df.to_csv(
    "outputs/daily_contributions_CLG_AllAccounts.csv", index=False)
