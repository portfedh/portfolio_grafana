# Script to delete any data at closing.

import mysql.connector

# Connect to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password1")

# Instantiate cursor
mycursor = mydb.cursor()

# Create Database
mycursor.execute("DROP DATABASE IF EXISTS user1_database")
