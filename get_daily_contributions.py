from sqlalchemy import create_engine
from scripts import daily_balance as db

# MySQL Connection Settings
###########################
engine = create_engine(
    'mysql+pymysql://root:password1@localhost:3306/PCL_database')

# CETES Account
###############
# Get contribution balance
contribution_balance_df = db.create_df(
    'inputs/pcl/contributions_PCL_CETES.csv')

# Create daily balance.
daily_contribution_balance_df = db.daily_balance(
    df=contribution_balance_df,
    column_name='Contribuciones_Cetes_MXN',
    sum=True)

# Output to CSV
daily_contribution_balance_df.to_csv(
    "outputs/daily_contributions_PCL_CETES.csv",
    index=True, index_label='Date')

# Output to MySQL
daily_contribution_balance_df.to_sql(
    name='daily_contributions_PCL_CETES',  # Table name
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# GBM Account
###############
# Get monthly balance
contribution_balance_df2 = db.create_df(
    'inputs/pcl/contributions_PCL_GBM.csv')

# Create daily balance
daily_contribution_balance_df2 = db.daily_balance(
    df=contribution_balance_df2,
    column_name='Contribuciones_GBM_MXN',
    sum=True)

# Output to CSV
daily_contribution_balance_df2.to_csv(
    "outputs/daily_contributions_PCL_GBM.csv",
    index=True, index_label='Date')

# Output to MySQL
daily_contribution_balance_df2.to_sql(
    name='daily_contributions_PCL_GBM',  # Table name
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')

# Sum both Accounts
###################
# Get total daily balance
total_contributions_df = db.consolidate(
    file_name_1='outputs/daily_contributions_PCL_CETES.csv',
    file_name_2='outputs/daily_contributions_PCL_GBM.csv',
    sum_col_name='Tot_Contribuciones_MXN')

# Outputs
#########
# Output to CSV
total_contributions_df.to_csv(
    "outputs/daily_contributions_PCL_AllAccounts.csv", index=False)

# Output to MySQL
total_contributions_df2 = db.create_df(
    'outputs/daily_contributions_PCL_AllAccounts.csv')

total_contributions_df2.to_sql(
    name='daily_contributions_PCL_AllAccounts',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
