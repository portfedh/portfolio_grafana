import mysql.connector

# Connect to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password1")

# Instantiate cursor
mycursor = mydb.cursor()

# Create Database
mycursor.execute("DROP DATABASE IF EXISTS PCL_database")
mycursor.execute("CREATE DATABASE PCL_database")

# Use Database
mycursor.execute("USE PCL_database")

# Create Tables:
# dict = {table_name: column_name}

# Create INT Tables: Daily account balance, Daily contributions, IRR
int_dict = {
    'daily_acct_balance_PCL_AllAccounts': 'Tot_Acct_Portafolio_MXN',
    'daily_acct_balance_PCL_CETES': 'Tot_Acct_Cetes_MXN',
    'daily_acct_balance_PCL_GBM': 'Tot_Acct_GBM_MXN',
    'daily_acct_balance_PCL_IBKR': 'Tot_Acct_IBKR_MXN',
    'daily_contributions_PCL_AllAccounts': 'Tot_Contribuciones_MXN',
    'daily_contributions_PCL_CETES': 'Contribuciones_Cetes_MXN',
    'daily_contributions_PCL_GBM': 'Contribuciones_GBM_MXN',
    'irr_contributions_PCL_AllAccounts': 'Tot_Contribuciones_MXN',
    'irr_monthly_account_balance_PCL_AllAccounts': 'Tot_Acct_Portafolio_MXN',
    }

for x, y in int_dict.items():
    mycursor.execute(f"DROP TABLE IF EXISTS {x}")
    mycursor.execute(
        f"CREATE TABLE {x} "
        f"(Date TIMESTAMP, {y} INT)")

# Create Float Table: XIRR
float_dict = {'irr_xirr_PCL': 'XIRR'}

for x, y in float_dict.items():
    mycursor.execute(f"DROP TABLE IF EXISTS {x}")
    mycursor.execute(
        f"CREATE TABLE {x} "
        f"(Date TIMESTAMP, {y} FLOAT)")

# Create two column tables: Returns
return_dict = {
    'returns_portfolio_PCL_AllAccounts':
    ['Tot_Portfolio_Return_MXN', 'Tot_Portfolio_Return_Percent']
    }

for x, y in return_dict.items():
    mycursor.execute(f"DROP TABLE IF EXISTS {x}")
    mycursor.execute(
        f"CREATE TABLE {x} "
        f"(Date TIMESTAMP, {y[0]} INT, {y[1]} FLOAT)")
