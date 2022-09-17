# daily_balance.py
"""
Get daily balances for all accounts.

This module takes monthly balances for each account as inputs and
consolidates them to return a total daily balance for all accounts.

The module contains the following functions:

- create_df(file_name):
    Returns an pandas df with values and dates in datetime format.

- daily_balance(df, column_name, sum):
    Returns a df with daily values from a monthly balance.

- add_df(*args):
    Returns a DataFrame appending all the columns in the input DataFrames.

- add_total_column(df, col_name):
    Returns a DataFrame with a total column, adding all column values.
"""


import pandas as pd


def create_df(file_name: str) -> 'pd':
    """
    Takes a csv file and returns a df with its index in datetime format.

    Input csv file must have two columns: Date column and values column.

        Parameters:
            filename:
                - csv file name, including file extension.
                  'path/filename.csv'

        Returns:
            df: DataFrame with two columns:
                - 'Date' column as the index, in datetime format.
                - Column Values, int or float.
    """
    df = pd.read_csv(file_name)
    # Create list from 'Date' column
    datetime_list = pd.to_datetime(
        df['Date'], dayfirst=True)
    # Make 'Date' column an index object
    datetime_list = pd.DatetimeIndex(datetime_list.values)
    # Append new 'Date' column to DataFrame, as index
    df = df.set_index(datetime_list)
    # Add 'Date' label to index column
    df = df.rename_axis('Date', axis=1)
    # Drop original 'Date' column
    df.drop('Date', axis=1, inplace=True)
    return df


def daily_balance(df: 'pd', column_name: str, sum: bool, range) -> 'pd':
    """
    Takes as input a monthly account balance and produces a daily balance.

    Uses a df with dates and monthly values and returns a df with daily values.
    Uses the output of create_df() function as input.

        Parameters:
            df:
                - Input DataFrame.
                - Must contain a date column in datetime format.
                - Must contain a column with values.

            column_name:
                - Must be the name of the column with values in df.

            sum:
                - True: Will add the values up to date.
                - False: Will append the latest value.

            range:
                - Date range for the daily balance

        Returns:
            daily_df:
                'Date' column as index in datetime format.
                column_name: Values.
    """
    # Create output DataFrame
    daily_df = pd.DataFrame(columns=[column_name])
    for date in range:
        # Filter DataFrame up to date
        filtered_balance_df = df.loc[:date]
        if sum is True:
            # Get the sum of values to date
            value = filtered_balance_df[column_name].sum()
        else:
            # Get last value
            try:
                value = filtered_balance_df[column_name].iloc[-1]
            except IndexError:
                # In case the df is empty at that date
                value = 0
        # Create dictionary with value
        new_dic_row = {column_name: value}
        # Create DataFrame from dictionary
        new_row_df = pd.DataFrame(new_dic_row, index=[date])
        # Merge with output DataFrame
        daily_df = pd.concat(
            [new_row_df, daily_df])
    # Set column from string to integer
    daily_df[column_name] = (
        daily_df[column_name].astype(int))
    # Add 'Date' label to the index column
    daily_df = daily_df.rename_axis(
        'Date', axis=1)
    return daily_df


# Same as merge_df() in irr_calculations.py. Eliminate merge_df().
def add_df(*args: pd) -> 'pd':
    """
    Returns a DataFrame appending all the columns in the input DataFrames.

        Parameters:
            *args:
                - Unlimited csv file names, including file extensions.
                    Example:
                        'path/filename.csv'
        Returns:
            df:
                - 'Date' column as index in datetime format.
                - Other columns: Added values
    """
    list = []
    for df in args:
        list.append(df)
    return pd.concat(list, axis=1)


def add_total_column(df, col_name):
    """
    Returns a DataFrame with a total column, adding all column values.

    Parameters:
        df:
            - DataFrame with amounts.
                Example:
                    Column0: 'Date'
                    Column1: 'Amount1'
                    Column2: 'Amount2'
    Returns:
        df:
            - DataFrame without duplicate columns
                Example:
                    Column0: 'Date'
                    Column1: 'Amount1'
                    Column2: 'Amount2'
                    Column2: 'Total'  (Amount1+Amount2)
    """
    df[col_name] = df.sum(axis=1)
    return df
