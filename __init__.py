# __init__.py
"""Calculates daily balances, share amounts, IRR and returns for a portfolio.

Modules in this package:

Scripts:
Functions that transform inputs into outputs.
    - daily_balance.py: Functions to get daily balances for all accounts.
    - daily_shares.py: Functions to get daily shares for all accounts.
    - irr_calculations.py: Functions to get xirr for the portfolio.
    - return_calculations.py: Functions to calculate the portfolio returns.

Inputs:
Files where user data will be stored:
    - Contributions CSV files
    - Account balance CSV files
    - Trading history CSV files

Outputs:
CSV Output files to check the data stored in MySQL.
    - Daily balances
    - Daily contributions
    - Daily shares
    - Daily prices
    - Daily subtotals
    - Daily returns
"""
