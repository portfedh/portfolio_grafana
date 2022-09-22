# irr_calculations.py
"""
This module contains functions used to calculate the IRR of the portfolio.

To calculate, it uses the consolidated contributions file and
the last value in the consolidated account balance file as inputs.

The module contains the following functions:

Irr contributions functions:
    - change_column_to_datetime(df, date_column)
        Change DataFrame date column to datetime format and make it the index.

    - filter_df_by_column(df: pd, columns: list
        Filter DataFrame. Only keep columns in provided list.

    - invert_df_column_values(df, column_name)
        Invert DataFrame column values by multiplying its values by (-1).

    - change_column_to_integers(df, column_name)
        Change a DataFrame column to to integers.

IRR Calculations:
    - get_last_row_of_df(df)
         Get the last row from a pandas DataFrame.

    - rename_df_column(df, balance_column, contributions_column)
        Rename the balance column like the contributions column.

    - split_df_into_two_lists(df, contributions_column)
        Separate the DataFrame into two lists: date_list and values_list.
"""

import pandas as pd


# irr_contributions functions
#############################

# Like daily_balance but does not require csv
def change_column_to_datetime(df: pd, date_column: str) -> pd:
    """
    Change DataFrame date column to datetime format and make it the index.
        Parameters:
            df: Input DataFrame
            date_column: Name of the column with dates.

        Returns:
            df: DataFrame with date_column as index and datetime format.
    """
    datetime_date = pd.to_datetime(df[date_column], dayfirst=True)
    datetime_index_trades = pd.DatetimeIndex(datetime_date.values)
    df = df.set_index(datetime_index_trades)
    df = df.rename_axis(date_column, axis=1)
    df.drop(date_column, axis=1, inplace=True)
    return df


def filter_df_by_column(df: pd, columns: list) -> pd:
    """
    Filter DataFrame. Only keep columns in provided list.

        Parameters:
            df: Input DataFrame
            columns: String or list of strings with columns to keep.

        Returns:
            df: DataFrame with index and selected columns in list.
    """
    df = df.filter(columns)
    return df


def invert_df_column_values(df: pd, column_name: str) -> pd:
    """
    Invert DataFrame column values by multiplying its values by (-1).

        Parameters:
            df: Input DataFrame
            column_name: Name of column to multiply values.
        Returns:
            df: DataFrame with values of column_name multiplied by (-1).
    """
    df[column_name] = df[column_name]*-1
    return df


# Can be eliminated if DataFrame has date as index
# Simply run:
# df = df.astype('int')
def change_column_to_integers(df: pd, column_name: str) -> pd:
    """
    Change a DataFrame column to to integers.

        Parameters:
            df: Input DataFrame.
            column_name: Name of the column to be changed.
        Returns:
            df: Output DataFrame with changed column.
    """
    df[column_name] = df[column_name].astype('int')
    return df


# IRR Calculations
##################

def get_last_row_of_df(df: pd) -> pd:
    """
    Get the last row from a pandas DataFrame.

        Parameters:
            df: Input dataframe.
        Returns:
            df: Output DataFrame with only last row.
    """
    df = df.iloc[-1:]
    return df


def rename_df_column(df: pd, balance_col: str, contributions_col: str) -> pd:
    """
    Rename the balance column like the contributions column.

        Parameters:
            df: Input DataFrame.
            balance_col: Column name with account balances.
            contributions_col: Column name with account contributions.
        Returns:
            df: Output DataFrame with changed column names.
    """
    df = df.rename(columns={balance_col: contributions_col})
    return df


def split_df_into_two_lists(df: pd, contributions_column: str) -> pd:
    """
    Separate the DataFrame into two lists: date_list and values_list.

        Parameters:
            df: Input DataFrame.
            contributions_column: Name of the contributions column..
        Returns:
            date_list: List with all the dates in the DataFrame.
            values_list: List with all the values in the contributions_column.
    """
    date_list = df.index.tolist()
    values_list = list(df[contributions_column])
    return date_list, values_list
