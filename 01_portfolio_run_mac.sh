#!/bin/bash

# Bash script to execute all python scripts

echo "Cleaning outputs directory:"
rm -v outputs/*

echo "Setting Up Docker files:"
docker pull portfedh/portfolio_dashboard:pcl_grafana
docker-compose up -d
sleep 5
echo

echo "Executing Portfolio Scripts:"

echo "    - Executing set_mysql_setup."
./venv/bin/python3 set_mysql_setup.py

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
./venv/bin/python3 get_daily_subtotals_perbankacct.py
./venv/bin/python3 get_daily_subtotals_allaccounts.py

echo "All scripts executed."
