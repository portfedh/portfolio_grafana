import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password1"
)

mycursor = mydb.cursor()

# Create Database
mycursor.execute("DROP DATABASE IF EXISTS test_database")
mycursor.execute("CREATE DATABASE test_database")

# Show Databases
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#    print(x)

# Use Database
mycursor.execute("USE test_database")

# Setup Tables
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

# Show tables
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)
