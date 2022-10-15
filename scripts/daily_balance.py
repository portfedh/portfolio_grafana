# daily_balance.py
"""
This module contains the functions to transform monthly balances for each
account as inputs and return a daily total balance.

The functions are also used by by other scripts in their calculations.

The module contains the following functions:

- create_df(file_name):
    Takes a csv file and returns a pandas df with its index in datetime format.

- create_daily_balance_df(df, column_name, sum):
    Returns a df with daily values from a monthly balance.

- concat_df(*args):
    Returns a DataFrame appending  rows or columns to the input DataFrame.

- add_total_column(df, col_name):
    Returns a DataFrame with appended total column, adding all column values.
"""


import pandas as pd


def create_df(file_name: str) -> 'pd':
    """
    Takes a csv file and returns a pandas df with its index in datetime format.

    Input csv file must have two columns: 'Date' column and values column.

        Parameters:
            filename:
                csv file name, including file extension.
                example: 'path/filename.csv'

        Returns:
            DataFrame with two columns:
                    'Date' column as the index, in datetime format.
                    Column values as int or float.
    """
    df = pd.read_csv(file_name)
    # Create list from 'Date' column
    datetime_list = pd.to_datetime(
        df['Date'], dayfirst=True, utc=True)
    # Make 'Date' column an index object
    datetime_list = pd.DatetimeIndex(datetime_list.values)
    # Append new 'Date' column to DataFrame, as index
    df = df.set_index(datetime_list)
    # Add 'Date' label to index column
    df = df.rename_axis('Date', axis=1)
    # Drop original 'Date' column
    df.drop('Date', axis=1, inplace=True)
    return df


def create_daily_balance_df(
        df: 'pd', column_name: str, sum: bool, range) -> 'pd':
    """
    Takes as input a monthly account balance and returns a daily balance.

    Uses a df with dates and monthly values as input.
    Returns a df with daily values as output.

        Parameters:
            df:
                Input DataFrame.
                Must contain a date column in datetime format.
                Must contain a column with values.

            column_name:
                Name of the column with values in output df.

            sum:
                True: Will add the values up to a date.
                False: Will append the latest value.

            range:
                Date range for the daily balance

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


def concat_df(*args: pd, type: int) -> 'pd':
    """
    Returns a DataFrame appending  rows or columns to the input DataFrame.

        Parameters:
            *args:
                Unlimited DataFrames.
            type:
                0: Concatenate rows.
                1: Concatenate columns.
        Returns:
            df:
                'Date' column as index in datetime format.
                Other columns: with values.
    """
    list = []
    for df in args:
        list.append(df)
    # Concatenate
    result = pd.concat(list, axis=type)
    # Substitute NA values with zeros
    result = result.fillna(0)
    return result


def add_total_column_to_df(df: pd, col_name: str) -> pd:
    """
    Returns a DataFrame with appended total column, adding all column values.

    Parameters:
        df: Input DataFrame with amounts.
                Example:
                    Column_0: 'Date'
                    Column_1: 'Amount_1'
                    Column_2: 'Amount_2'
        col_name:
            Name of the column with added values.
            In example below: 'Total'
    Returns:
        df: DataFrame with new column and total amounts
                Example:
                    Column_0: 'Date'
                    Column_1: 'Amount_1'
                    Column_2: 'Amount_2'
                    Column_3: 'Total'  (Amount_1+Amount_2)
    """
    df[col_name] = df.sum(axis=1)
    return df
