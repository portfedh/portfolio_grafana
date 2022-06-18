# daily_balance.py
"""Provide calculations to get daily balances for all accounts.

This module allows the user get daily balances for each account
and consolidate  to get a total daily balance for all accounts.

The module contains the following functions:

- create_df(file_name):
    Returns pandas df with values and dates in datetime format.

- daily_balance(df, column_name, sum):
    Returns daily values from monthly balance.

- consolidate (file_name_1, file_name_2, sum_col_name):
    Returns pandas df with added amounts of two daily balances.
"""


import pandas as pd
import set_analysis_dates


def create_df(file_name: str) -> 'pd':
    """
    Takes a CSV file and returns a df with an index in datetime format.

    Input CSV File must have two columns: Date column and value column.

        Parameters:
            filename:
                String with input CSV <path/filename.csv>.

        Returns:
            df: Dataframe with two columns:
                'Date' column as the index, in datetime format.
                Column Values, int or float.
    """
    df = pd.read_csv(file_name)
    # Create list from 'Date' column
    datetime_list = pd.to_datetime(
        df['Date'], dayfirst=True)
    # Make 'Date' column an index object
    datetime_list = pd.DatetimeIndex(datetime_list.values)
    # Append new 'Date' column to dataframe, as index
    df = df.set_index(datetime_list)
    # Add 'Date' label to index column
    df = df.rename_axis('Date', axis=1)
    # Drop original 'Date' column
    df.drop('Date', axis=1, inplace=True)
    return df


def daily_balance(df: 'pd', column_name: str, sum: bool) -> 'pd':
    """
    Will take the monthly account balance and produce a daily balance.

    Takes a df with dates and values and returns a df with daily values.
    Uses the return df from 'create_df function' as input.

        Parameters:
            df:
                Input Dataframe.
                Must have a date column in datetime format.
                Must have a value column.
            column_name:
                Must be equal to the name of the column in df.
            sum:
                True: Will add values up to each date.
                False: Will append the latest value.

        Returns:
            daily_df: pd.
                'Date' column as index in datetime format.
                column_name: int. Values
    """
    # Create output dataframe
    daily_df = pd.DataFrame(columns=[column_name])
    for date in set_analysis_dates.date_range:
        # Filter dataframe up to date
        filtered_blance_df = df.loc[:date]
        if sum is True:
            # Get the sum of values to date
            value = filtered_blance_df[column_name].sum()
        else:
            # Get last value
            value = filtered_blance_df[column_name].iloc[-1]
        # Create dictionary with value
        new_dic_row = {column_name: value}
        # Create dataframe from dictionary
        new_row_df = pd.DataFrame(new_dic_row, index=[date])
        # Merge with output dataframe
        daily_df = pd.concat(
            [new_row_df, daily_df])
    # Set column from string to integer
    daily_df[column_name] = (
        daily_df[column_name].astype(int))
    # Add 'Date' label to the index column
    daily_df = daily_df.rename_axis(
        'Date', axis=1)
    return daily_df


def consolidate(file_name_1: str, file_name_2: str, sum_col_name: str) -> 'pd':
    """
    Will consolidate the daily balance of two accounts and show total values.

    Takes two df and returns a new df with the added column values.

        Parameters:
            file_name_1:
                String with CSV <path/filename.csv>.
            file_name_2:
                String with CSV <path/filename.csv>.
            sum_col_name:
                Name of the column that adds the values from file1 & file2.

        Returns:
            df_total: df
                'Date' column as index in datetime format.
                sum_col_name: int. Added values
    """
    # Get balances from CSVs
    df_1 = pd.read_csv(file_name_1)
    df_2 = pd.read_csv(file_name_2)
    # Merge dataframes
    df_total = df_1.copy()
    column_name = df_2.columns[1]
    df_total[column_name] = df_2[[column_name]].copy()
    # Add Total Values
    df_total[sum_col_name] = (
        df_total[df_total.columns[1]] + df_total[df_total.columns[2]])
    # Drop other columns
    df_total.drop(
        columns=[df_total.columns[1], df_total.columns[2]], inplace=True)
    return df_total
