#!/bin/bash

# Script to delete the MySQL database, 
# all csv files and close down docker.

echo "Removing MySQL Database:"
./venv_linux/bin/python3 set_mysql_close.py
echo

echo "Removing Docker files:"
docker-compose down
echo

echo "Removing all CSV files:"
rm -v outputs/*

echo "All files removed succesfully."