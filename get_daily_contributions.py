from scripts import daily_balance as dcb

# CETES Account
###############
# Get contribution balance
contribution_balance_df = dcb.create_df(
    'inputs/contributions_CLG_CETES.csv')

# Create daily balance.
daily_contribution_balance_df = dcb.daily_balance(
    df=contribution_balance_df,
    column_name='Contribuciones_Cetes_MXN',
    sum=True)

# Output to CSV
daily_contribution_balance_df.to_csv(
    "outputs/daily_contributions_CLG_CETES.csv",
    index=True, index_label='Date')


# GBM Account
###############
# Get monthly balance
contribution_balance_df2 = dcb.create_df(
    'inputs/contributions_CLG_GBM.csv')

# Create daily balance
daily_contribution_balance_df2 = dcb.daily_balance(
    df=contribution_balance_df2,
    column_name='Contribuciones_GBM_MXN',
    sum=True)

# Output to CSV
daily_contribution_balance_df2.to_csv(
    "outputs/daily_contributions_CLG_GBM.csv",
    index=True, index_label='Date')

# Sum both Accounts
###################
# Get total daily balance
total_contributions_df = dcb.consolidate(
    file_name_1='outputs/daily_contributions_CLG_CETES.csv',
    file_name_2='outputs/daily_contributions_CLG_GBM.csv',
    col_name='Tot_Contribuciones_MXN')

# Output to CSV
total_contributions_df.to_csv(
    "outputs/daily_contributions_CLG_AllAccounts.csv", index=False)
