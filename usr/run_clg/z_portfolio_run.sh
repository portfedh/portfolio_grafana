#!/bin/bash

echo "Cleaning outputs directory:"
rm -v outputs/*

echo "Setting Up Docker files:"
docker-compose up -d
sleep 5
echo

echo "Executing Portfolio Scripts:"

echo "    - Executing set_mysql_setup."
./venv/bin/python3 set_mysql_setup.py

echo "    - Executing set_analysis_dates."
./venv/bin/python3 set_analysis_dates.py

echo "    - Executing get_daily_balance."
./venv/bin/python3 get_daily_balance.py

echo "    - Executing get_daily_contributions."
./venv/bin/python3 get_daily_contributions.py

echo "    - Executing get_irr."
./venv/bin/python3 get_irr.py

echo "    - Executing get_returns."
./venv/bin/python3 get_returns.py

echo "    - Executing get_daily_shares."
./venv/bin/python3 get_daily_shares.py

echo "    - Executing get_daily_prices."
./venv/bin/python3 get_daily_prices.py

echo "    - Executing get_daily_subtotals."
./venv/bin/python3 get_daily_subtotals.py

echo "    - Executing get_daily_percentages."
./venv/bin/python3 get_daily_percentages.py

echo "All scripts executed successfully."
