import pandas as pd
from sqlalchemy import create_engine
from scripts import daily_balance as db

# MySQL Connection Settings
###########################
url = 'mysql+pymysql://root:password1@localhost:3306/PCL_database'
engine = create_engine(url)

# Imports
#########
# Import CSV files and create data frames
shares_df = db.create_df('outputs/daily_share_quantity_PCL_GBM.csv')
prices_df = db.create_df('outputs/daily_prices_interpolated_PCL_GBM.csv')
cetes_df = db.create_df('outputs/daily_acct_balance_PCL_CETES.csv')

# Transformations
#################
# Rename columns: Add Quantity or price simbol
shares_df = shares_df.add_prefix('Q_')
prices_df = prices_df.add_prefix('P_')
# Rename columns: Remove .MX to avoid problems in SQL
shares_df.columns = shares_df.columns.str.removesuffix('.MX')
prices_df.columns = prices_df.columns.str.removesuffix('.MX')
# Merge Dataframes
new_df = pd.concat(([shares_df, prices_df, cetes_df]), axis=1)

# Interpolate missing values (prices are NaN on weekend dates)
df_interpol = new_df.interpolate(method='linear', limit_direction='both')

# Portfolio Calculations
########################
# Subtotals ($)
ticker_list = ['VGK', 'IEMG', 'VTI', 'BNDX', 'BND', 'VPL', 'VOO', 'SHV',
               'MCHI', 'GOLDN', 'FIBRAPL14', 'BABAN', 'PG', 'INTC']

for x in ticker_list:
    df_interpol[f'Sub_{x}'] = (
        df_interpol[f'Q_{x}'] *
        df_interpol[f'P_{x}'])

# Total Fixed Income GBM ($)
df_interpol['Tot_FixedIncome_GBM'] = (
    df_interpol['Sub_BNDX'] +
    df_interpol['Sub_BND'] +
    df_interpol['Sub_SHV'])

# Total Fixed Income GBM + CETES ($)
df_interpol['Tot_FixedIncome'] = (
    df_interpol['Sub_BNDX'] +
    df_interpol['Sub_BND'] +
    df_interpol['Sub_SHV'] +
    df_interpol['Tot_Acct_Cetes_MXN'])

# Total Equity ($)
df_interpol['Tot_Equity'] = (
    df_interpol['Sub_VGK'] +
    df_interpol['Sub_IEMG'] +
    df_interpol['Sub_VTI'] +
    df_interpol['Sub_VPL'] +
    df_interpol['Sub_VOO'] +
    df_interpol['Sub_MCHI'] +
    df_interpol['Sub_BABAN'] +
    df_interpol['Sub_PG'] +
    df_interpol['Sub_INTC'])

# Total Alternatives ($)
df_interpol['Tot_Alternatives'] = (
    df_interpol['Sub_GOLDN'] +
    df_interpol['Sub_FIBRAPL14'])

# Total  Portafolio ($)
df_interpol['Tot_Portfolio'] = (
    df_interpol['Tot_Equity'] +
    df_interpol['Tot_FixedIncome'] +
    df_interpol['Tot_Alternatives'])

# ############ Check this############
# Reorder Column Position
my_column = df_interpol.pop('Tot_Acct_Cetes_MXN')
df_interpol.insert(31, my_column.name, my_column)

# Remove Quantity and Price Columns
df_interpol.drop(df_interpol.iloc[:, 0:20], inplace=True, axis=1)

# Outputs
#########
# Output to CSV
df_interpol.to_csv(
    "outputs/daily_subtotals_PCL_AllAccounts.csv",
    index=True,
    index_label='Date')

# Output to MySQL
df_interpol.to_sql(
    name='daily_subtotals_PCL_GBM',
    con=engine,
    if_exists='replace',
    index=True, index_label='Date')
