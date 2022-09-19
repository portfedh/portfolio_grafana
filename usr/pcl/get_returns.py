# Script to calculate the portfolio return in $ and % amounts.

from pyxirr import xirr
from set_engine import engine
import move_two_levels_up
from scripts import daily_balance as db
from scripts import irr_calculations as irr
from scripts import return_calculations as rc

# Create Portfolio Returns
##########################

# Variables
contributions = db.create_df(
    'outputs/daily_contributions_PCL_AllAccounts.csv')
balance = db.create_df(
    'outputs/daily_acct_balance_PCL_AllAccounts.csv')
col_contrb = 'Tot_Contribuciones_MXN'
col_balance = 'Tot_Acct_Portafolio_MXN'
col_return = 'Tot_Portfolio_Return_MXN'
col_ratio = 'Tot_Portfolio_Return_Percent'

# Merge daily contributions and daily balance DataFrames
return_df = db.concat_df(contributions, balance, type=1)

# Create column with the portfolio return $
return_df = rc.subtract_columns_in_df(
    df=return_df,
    column1=col_balance,
    column2=col_contrb,
    subtraction_col=col_return)

# Save column data as Integer
return_df = irr.change_column_to_integers(return_df, col_return)

# Create column with the portfolio return %
return_df = rc.add_ratio_column_in_df(
    df=return_df,
    column_name=col_ratio,
    column2=col_balance,
    column1=col_contrb)

# Outputs
#########
# Save value to CSV
filename = 'outputs/returns_portfolio_PCL_AllAccounts.csv'
return_df.to_csv(filename, index=True, index_label='Date')

# Save value to MySQL
returns_mysql = db.create_df(filename)
table_name = 'returns_portfolio_PCL_AllAccounts'
returns_mysql.to_sql(name=table_name, con=engine, if_exists='replace',
                     index=True, index_label='Date')
