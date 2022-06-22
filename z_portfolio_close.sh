#!/bin/bash

echo "Removing MySQL Database:"
./venv/bin/python3 set_mysql_close.py
echo

echo "Removing Docker files:"
docker-compose down
echo

echo "Removing all CSV files:"
rm -v outputs/*

echo "All files removed succesfully."