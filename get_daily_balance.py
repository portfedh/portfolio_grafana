from scripts import daily_balance as dab

# CETES Account
###############
# Get monthly balance
balance_df2 = dab.create_df('inputs/monthly_account_balance_CLG_CETES.csv')

# Create daily balance
daily_balance_df2 = dab.daily_balance(
    df=balance_df2,
    column_name='Tot_Acct_Cetes_MXN',
    sum=False)

# Output to CSV
daily_balance_df2.to_csv(
    "outputs/daily_acct_balance_CLG_CETES.csv",
    index=True, index_label='Date')


# GBM Account
#############
# Get monthly balance
balance_df = dab.create_df('inputs/monthly_account_balance_CLG_GBM.csv')

# Create daily balance
daily_balance_df = dab.daily_balance(
    df=balance_df,
    column_name='Tot_Acct_GBM_MXN',
    sum=False)

# Output to CSV
daily_balance_df.to_csv(
    "outputs/daily_acct_balance_CLG_GBM.csv",
    index=True, index_label='Date')

# Sum both Accounts
###################
# Get total daily balance
total_balance_df = dab.consolidate(
    file_name_1='outputs/daily_acct_balance_CLG_CETES.csv',
    file_name_2='outputs/daily_acct_balance_CLG_GBM.csv',
    col_name='Tot_Acct_Portafolio_MXN')

# Output to CSV
total_balance_df.to_csv(
    "outputs/daily_acct_balance_CLG_AllAccounts.csv",
    index=False)
