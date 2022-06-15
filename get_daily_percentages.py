import set_portfolio_targets as t
from sqlalchemy import create_engine
from scripts import daily_balance as db

# MySQL Connection Settings
###########################
engine = create_engine(
    'mysql+pymysql://root:password1@localhost:3306/CLG_database')

# Imports
#########
# Import CSV files and create data frames
subtotals_df = db.create_df('outputs/daily_subtotals_CLG_AllAccounts.csv')

# Portfolio Calculations
########################
# Total Equity (%)
subtotals_df['Tot_Equity_PCT'] = (
    subtotals_df['Tot_Equity'] / subtotals_df['Tot_Portfolio'])
# Calculando Total Fixed Income(%)
subtotals_df['Tot_FixedIncome_PCT'] = (
    subtotals_df['Tot_FixedIncome'] / subtotals_df['Tot_Portfolio'])
# Calculando Total Alternatives(%)
subtotals_df['Tot_Alternatives_PCT'] = (
    subtotals_df['Tot_Alternatives'] / subtotals_df['Tot_Portfolio'])

# Target Equity(%)
subtotals_df['Target_Equity_PCT'] = t.target_equity
# Target Fixed Income(%)
subtotals_df['Target_FixedIncome_PCT'] = t.target_fixed_income
# Target Fixed Alternatives(%)
subtotals_df['Target_Alternatives_PCT'] = t.target_alternatives

# Remove Quantity and Price Columns
subtotals_df.drop(subtotals_df.iloc[:, 0:16], inplace=True, axis=1)

# Outputs
#########
# Output to CSV
subtotals_df.to_csv(
    "outputs/daily_percentages_CLG_GBM.csv",
    index=True,
    index_label='Date')

# Output to MySQL
subtotals_df.to_sql(
    name='daily_percentages_CLG_GBM',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
