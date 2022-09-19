# irr_calculations.py
"""
Functions used to calculate the IRR of the portfolio.

Uses consolidated contributions file and the last value in
the consolidated account balance file as inputs.

The module contains the following functions:

Irr contributions functions:
    - concat_df(*args)
        Concatenate unlimited DataFrames

    - to_datetime_df(df, date_column)
        Turn date to datetime format

    - filter_df(df: pd, columns: list
        Filter df to keep columns in list

    - invert_cf_df(df, column_name)
        Invert values as cash flows

    - integers_df(df, column_name)
        Save values as integers

IRR Calculations:
    - get_last_value(df)
        Get las value from a pandas DataFrame

    - rename_column(df, balance_column, contributions_column)
        Rename the balance column like the contributions column

    - split_df(df, contributions_column)
        Separate the DataFrame into two lists for the xirr function
"""

import pandas as pd


# irr_contributions functions
#############################

# Like daily_balance but does not require csv
def change_column_to_datetime(df: pd, date_column: pd) -> pd:
    """Turn date to datetime format"""
    datetime_date = pd.to_datetime(df[date_column], dayfirst=True)
    datetime_index_trades = pd.DatetimeIndex(datetime_date.values)
    df = df.set_index(datetime_index_trades)
    df = df.rename_axis(date_column, axis=1)
    df.drop(date_column, axis=1, inplace=True)
    return df


# Check if column variable can be changed to a string
# df = df.filter([columns])
def filter_df_by_column(df: pd, columns: list) -> pd:
    "Filter df to keep columns in list"
    df = df.filter(columns)
    return df


def invert_df_column_values(df: pd, column_name: str) -> pd:
    """Invert values as cash flows"""
    df[column_name] = df[column_name]*-1
    return df


# Can be eliminated if DataFrame has date as index
# Simply run:
# df = df.astype('int')
def change_column_to_integers(df: pd, column_name: str) -> pd:
    """Save values as integers"""
    df[column_name] = df[column_name].astype('int')
    return df


# IRR Calculations
##################

def get_last_row_of_df(df: pd) -> pd:
    """Get las value from a pandas DataFrame"""
    df = df.iloc[-1:]
    return df


def rename_df_column(df: pd, balance_col: str, contributions_col: str) -> pd:
    """Rename the balance column like the contributions column"""
    df = df.rename(columns={balance_col: contributions_col})
    return df


def split_df_into_two_lists(df: pd, contributions_column: str) -> pd:
    """Separate the DataFrame into two lists for the xirr function"""
    date_list = df.index.tolist()
    values_list = list(df[contributions_column])
    return date_list, values_list
