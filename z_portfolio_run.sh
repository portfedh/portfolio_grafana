#!/bin/bash

echo "Executing Portfolio Scripts."

echo "Executing set_mysql_setup."
./venv/bin/python3 set_mysql_setup.py

echo "Executing set_analysis_dates."
./venv/bin/python3 set_analysis_dates.py

echo "Executing get_daily_balance."
./venv/bin/python3 get_daily_balance.py

echo "Executing get_daily_contributions."
./venv/bin/python3 get_daily_contributions.py

echo "Executing get_irr."
./venv/bin/python3 get_irr.py

echo "Executing get_returns."
./venv/bin/python3 get_returns.py

echo "All scripts executed successfully."
