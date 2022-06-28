from sqlalchemy import create_engine
from scripts import daily_balance as db
from scripts import return_calculations as rc

# MySQL Connection Settings
###########################
url = 'mysql+pymysql://root:password1@localhost:3306/CLG_database'
engine = create_engine(url)

# Create Portfolio Returns
##########################
returns_df = rc.returns(
    contributions=db.create_df(
        'outputs/daily_contributions_CLG_AllAccounts.csv'),
    balance=db.create_df(
        'outputs/daily_acct_balance_CLG_AllAccounts.csv'),
    col_contrb='Tot_Contribuciones_MXN',
    col_balance='Tot_Acct_Portafolio_MXN',
    col_sub='Tot_Portfolio_Return_MXN',
    col_ratio='Tot_Portfolio_Return_Percent')

# Outputs
#########
# Save value to CSV
returns_df.to_csv(
    "outputs/returns_portfolio_CLG_AllAccounts.csv",
    index=True, index_label='Date')

# Save value to MySQL
returns_mysql = db.create_df('outputs/returns_portfolio_CLG_AllAccounts.csv')
returns_mysql.to_sql(
    name='returns_portfolio_CLG_AllAccounts',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
