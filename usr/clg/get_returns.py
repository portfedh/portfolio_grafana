# Script to calculate the portfolio return in $ and % amounts.

from set_engine import engine
import move_two_levels_up
from scripts import daily_balance as db
from scripts import return_calculations as rc

# Create Portfolio Returns
##########################

# Variables
contributions = db.create_df(
    'outputs/daily_contributions_CLG_AllAccounts.csv')
balance = db.create_df(
    'outputs/daily_acct_balance_CLG_AllAccounts.csv')
col_contrb = 'Tot_Contribuciones_MXN'
col_balance = 'Tot_Acct_Portafolio_MXN'
col_return = 'Tot_Portfolio_Return_MXN'
col_ratio = 'Tot_Portfolio_Return_Percent'

# Merge daily contributions and daily balance DataFrames
return_df = rc.merge_df(contributions, balance)

# Create column with the portfolio return $
return_df = rc.subtract_column(
    df=return_df,
    column1=col_balance,
    column2=col_contrb,
    subtraction_col=col_return)

# Save column data as Integer
return_df = rc.df_column_to_int(return_df, col_return)

# Create column with the portfolio return %
return_df = rc.add_ratio_column(
    df=return_df,
    column_name=col_ratio,
    column2=col_balance,
    column1=col_contrb)

# Drop calculation columns
return_df = rc.drop_column(return_df, col_contrb, col_balance)

# Outputs
#########
# Save value to CSV
filename = 'outputs/returns_portfolio_CLG_AllAccounts.csv'
return_df.to_csv(filename, index=True, index_label='Date')

# Save value to MySQL
returns_mysql = db.create_df(filename)
table_name = 'returns_portfolio_CLG_AllAccounts'
returns_mysql.to_sql(name=table_name, con=engine, if_exists='replace',
                     index=True, index_label='Date')
