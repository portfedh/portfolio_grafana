import pandas as pd
import set_portfolio_targets as t
from sqlalchemy import create_engine
from scripts import daily_balance as db

# MySQL Connection Settings
###########################
engine = create_engine(
    'mysql+pymysql://root:password1@localhost:3306/CLG_database')

# Import CSV files and create data frames
shares_df = db.create_df('outputs/daily_share_quantity_CLG_GBM.csv')
prices_df = db.create_df('outputs/daily_prices_interpolated_CLG_GBM.csv')
cetes_df = db.create_df('outputs/daily_acct_balance_CLG_CETES.csv')

# Rename columns
shares_df = shares_df.add_prefix('Q_')
prices_df = prices_df.add_prefix('P_')

# Merge Dataframes
new_df = pd.concat(([shares_df, prices_df, cetes_df]), axis=1)

# Interpolate missing values (prices are NaN on weekend dates)
df_interpol = new_df.interpolate(method='linear', limit_direction='both')

# Portfolio Calculations
########################

# Subtotals ($)
df_interpol['Sub_VOO.MX'] = (
    df_interpol['Q_VOO.MX'] *
    df_interpol['P_VOO.MX'])

df_interpol['Sub_VGK.MX'] = (
    df_interpol['Q_VGK.MX'] *
    df_interpol['P_VGK.MX'])

df_interpol['Sub_VPL.MX'] = (
    df_interpol['Q_VPL.MX'] *
    df_interpol['P_VPL.MX'])

df_interpol['Sub_IEMG.MX'] = (
    df_interpol['Q_IEMG.MX'] *
    df_interpol['P_IEMG.MX'])

df_interpol['Sub_MCHI.MX'] = (
    df_interpol['Q_MCHI.MX'] *
    df_interpol['P_MCHI.MX'])

df_interpol['Sub_GOLDN.MX'] = (
    df_interpol['Q_GOLDN.MX'] *
    df_interpol['P_GOLDN.MX'])

df_interpol['Sub_FIBRAPL14.MX'] = (
    df_interpol['Q_FIBRAPL14.MX'] *
    df_interpol['P_FIBRAPL14.MX'])

df_interpol['Sub_CETETRCISHRS.MX'] = (
    df_interpol['Q_CETETRCISHRS.MX'] *
    df_interpol['P_CETETRCISHRS.MX'])

df_interpol['Sub_IB1MXXN.MX'] = (
    df_interpol['Q_IB1MXXN.MX'] *
    df_interpol['P_IB1MXXN.MX'])

df_interpol['Sub_SHV.MX'] = (
    df_interpol['Q_SHV.MX'] *
    df_interpol['P_SHV.MX'])

# Total Fixed Income GBM ($)
df_interpol['Tot_FixedIncome_GBM'] = (
    df_interpol['Sub_CETETRCISHRS.MX'] +
    df_interpol['Sub_IB1MXXN.MX'] +
    df_interpol['Sub_SHV.MX'])

# Total Fixed Income GBM + CETES ($)
df_interpol['Tot_FixedIncome'] = (
    df_interpol['Sub_CETETRCISHRS.MX'] +
    df_interpol['Sub_IB1MXXN.MX'] +
    df_interpol['Sub_SHV.MX'] +
    df_interpol['Tot_Acct_Cetes_MXN'])

# Total Equity ($)
df_interpol['Tot_Equity'] = (
    df_interpol['Sub_VOO.MX'] +
    df_interpol['Sub_VGK.MX'] +
    df_interpol['Sub_VPL.MX'] +
    df_interpol['Sub_IEMG.MX'] +
    df_interpol['Sub_MCHI.MX'])

# Total Alternatives ($)
df_interpol['Tot_Alternatives'] = (
    df_interpol['Sub_GOLDN.MX'] +
    df_interpol['Sub_FIBRAPL14.MX'])

# Total  Portafolio ($)
df_interpol['Tot_Portfolio'] = (
    df_interpol['Tot_Equity'] +
    df_interpol['Tot_FixedIncome'] +
    df_interpol['Tot_Alternatives'])

# Total Equity (%)
df_interpol['Tot_Equity_PCT'] = (
    df_interpol['Tot_Equity'] / df_interpol['Tot_Portfolio'])
# Calculando Total Fixed Income(%)
df_interpol['Tot_FixedIncome_PCT'] = (
    df_interpol['Tot_FixedIncome'] / df_interpol['Tot_Portfolio'])
# Calculando Total Alternatives(%)
df_interpol['Tot_Alternatives_PCT'] = (
    df_interpol['Tot_Alternatives'] / df_interpol['Tot_Portfolio'])

# Target Equity(%)
df_interpol['Target_Equity_PCT'] = t.target_equity
# Target Fixed Income(%)
df_interpol['Target_FixedIncome_PCT'] = t.target_fixed_income
# Target Fixed Alternatives(%)
df_interpol['Target_Alternatives_PCT'] = t.target_alternatives

# Reorder Column Position
my_column = df_interpol.pop('Tot_Acct_Cetes_MXN')
df_interpol.insert(31, my_column.name, my_column)

# Output to CSV
df_interpol.to_csv(
    "outputs/daily_subtotals_CLG_AllAccounts.csv",
    index=True,
    index_label='Date')

# Output to MySQL
df_interpol.to_sql(
    name='daily_share_quantity_CLG_GBM',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
