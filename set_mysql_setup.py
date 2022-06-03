import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password1")

mycursor = mydb.cursor()

# Create Database
mycursor.execute("DROP DATABASE IF EXISTS CLG_database")
mycursor.execute("CREATE DATABASE CLG_database")

# Show Databases
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#    print(x)

# Use Database
mycursor.execute("USE CLG_database")

# Create Tables: Daily Account Balance
mycursor.execute(
    "DROP TABLE IF EXISTS \
    daily_acct_balance_CLG_AllAccounts")
mycursor.execute(
    "DROP TABLE IF EXISTS \
    daily_acct_balance_CLG_CETES")
mycursor.execute(
    "DROP TABLE IF EXISTS \
    daily_acct_balance_CLG_GBM")
mycursor.execute(
    "CREATE TABLE \
    daily_acct_balance_CLG_AllAccounts \
    (Date TIMESTAMP, Tot_Acct_Portafolio_MXN INT)")
mycursor.execute(
    "CREATE TABLE \
    daily_acct_balance_CLG_CETES \
    (Date TIMESTAMP, Tot_Acct_Cetes_MXN INT)")
mycursor.execute(
    "CREATE TABLE \
    daily_acct_balance_CLG_GBM \
    (Date TIMESTAMP, Tot_Acct_GBM_MXN INT)")

# Create Tables: Daily Contributions
mycursor.execute(
    "CREATE TABLE \
    daily_contributions_CLG_AllAccounts \
    (Date TIMESTAMP, Tot_Contribuciones_MXN INT)")
mycursor.execute(
    "CREATE TABLE \
    daily_contributions_CLG_CETES \
    (Date TIMESTAMP, Contribuciones_Cetes_MXN INT)")
mycursor.execute(
    "CREATE TABLE \
    daily_contributions_CLG_GBM \
    (Date TIMESTAMP, Contribuciones_GBM_MXN INT)")

# Create Tables: IRR
mycursor.execute(
    "CREATE TABLE \
    irr_xirr \
    (Date TIMESTAMP, XIRR INT)")
mycursor.execute(
    "CREATE TABLE \
    irr_contributions_CLG_AllAccounts \
    (Date TIMESTAMP, Tot_Contribuciones_MXN INT)")
mycursor.execute(
    "CREATE TABLE \
    irr_monthly_account_balance_CLG_AllAccounts \
    (Date TIMESTAMP, Tot_Acct_Portafolio_MXN INT)")

# Show tables
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)