# return_calculations.py
"""Calculates the return for the portfolio in $ and % amounts.

The module contains the following functions:

- merge_df(DataFrame1, DataFrame2):
    Merge DataFrame2 into DataFrame1

- subtract_column(df, column1, column2, subtraction_col):
    Create column with the subtraction of column2 from column1

- df_column_to_int(df, column):
    Transform column data to integers

- add_ratio_column(df, column_name, column2, column1):
    Create column with the ratio of column2 / column1

- drop_column(df: pd, *args: pd.column) -> pd:
    Drop columns from DataFrame

"""

import pandas as pd


def merge_df(DataFrame1: pd, DataFrame2: pd) -> pd:
    ''' Merge DataFrame2 into DataFrame1'''
    merged_df = DataFrame1.merge(
        DataFrame2, left_index=True, right_index=True)
    return merged_df


def subtract_column(
        df: pd,
        column1: str,
        column2: str,
        subtraction_col: str,
        ) -> pd:
    ''' Create column with the subtraction of column2 from column1'''
    df[subtraction_col] = (df[column1] - df[column2])
    return df


def df_column_to_int(df: pd, column: pd) -> pd:
    ''' Transform column data to integers '''
    df[column] = (df[column].astype('int'))
    return df


def add_ratio_column(
        df: pd,
        column_name: str,
        column2: pd,
        column1: pd
        ) -> pd:
    ''' Create column with the ratio of column2 / column1 '''
    df[column_name] = ((df[column2] / df[column1])-1)
    return df


def drop_column(df: pd, *args: pd) -> pd:
    ''' Drop columns from DataFrame '''
    df.drop(list(args), axis=1, inplace=True)
    return df
