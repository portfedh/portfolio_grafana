# irr_calculations.py
"""
Calculate the IRR of the portfolio.

Uses consolidated contributions and the last value in
the consolidated account balance.

The module contains the following functions:

Irr contributions functions
- concat_df(*args)
- to_datetime_df(df, date_column)
- add_total_df(df, col_name)
- filter_df(df: pd, columns: list
- invert_cf_df(df, column_name)
- integers_df(df, column_name)

Monthly balance functions
- merge_df(*args: pd)

IRR Calculations
- get_last_value(df)
- rename_column(df, balance_column, contributions_column)
- split_df(df, contributions_column)
"""

import pandas as pd


# irr_contributions functions
##############################################################################
def concat_df(*args):
    """Concatenate unlimited dataframes"""
    list = []
    for x in args:
        e = pd.read_csv(x)
        list.append(e)
    # Concatenate
    result = pd.concat(list, axis=0)
    # Substitute NA values with zeros
    result = result.fillna(0)
    return result


# Like daily_balance but does not require csv
def to_datetime_df(df, date_column):
    """Turn date to datetime format"""
    datetime_date = pd.to_datetime(df[date_column], dayfirst=True)
    datetime_index_trades = pd.DatetimeIndex(datetime_date.values)
    df = df.set_index(datetime_index_trades)
    df = df.rename_axis(date_column, axis=1)
    df.drop(date_column, axis=1, inplace=True)
    return df


def add_total_df(df, col_name):
    """Add total column to df"""
    df[col_name] = df.sum(axis=1)
    return df


# Check if column variable can be changed to a string
# df = df.filter([columns])
def filter_df(df: pd, columns: list):
    "Filter df to keep columns in list"
    df = df.filter(columns)
    return df


def invert_cf_df(df, column_name):
    """Invert values as cashflows"""
    df[column_name] = df[column_name]*-1
    return df


# Can be eliminated if dataframe has date as index
# Simply run:
# df = df.astype('int')
def integers_df(df, column_name):
    """Save values as integers"""
    df[column_name] = df[column_name].astype('int')
    return df


# Monthly Balance Functions
##############################################################################

# Very similar to concat_df but with axis=1 and without read CSV
def merge_df(*args: pd):
    """Merge unlimited dataframes"""
    list = []
    for x in args:
        list.append(x)
    # Concatenate
    result = pd.concat(list, axis=1)
    return result


# IRR Calculations
##############################################################################

# Get las value from pd dataframe
def get_last_value(df):
    df = df.iloc[-1:]
    return df


# Rename balance column like contributions column
def rename_column(df, balance_column, contributions_column):
    df = df.rename(columns={balance_column: contributions_column})
    return df


def split_df(df, contributions_column):
    # Separate df into two lists
    date_list = df.index.tolist()
    values_list = list(df[contributions_column])
    return date_list, values_list
