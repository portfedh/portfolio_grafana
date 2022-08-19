# return_calculations.py
"""Calculates the return for the portfolio in $ and % amounts.

The module contains the following functions:

- merge_df(dataframe1, dataframe2):
    Merge dataframe2 into dataframe1

- subtract_column(df, column1, column2, subtraction_col):
    Create column with the subtraction of column2 from column1

- df_column_to_int(df, column):
    Transform column data to integers

- add_ratio_column(df, column_name, column2, column1):
    Create column with the ratio of column2 / column1

- def drop_column(df: pd, *args: pd.column) -> pd:
    Drop columns from dataframe

"""

import pandas as pd


def merge_df(dataframe1: pd, dataframe2: pd) -> pd:
    ''' Merge dataframe2 into dataframe1'''
    merged_df = dataframe1.merge(
        dataframe2, left_index=True, right_index=True)
    return merged_df


def subtract_column(
        df: pd,
        column1: pd.column,
        column2: pd.column,
        subtraction_col: pd.column,
        ) -> pd:
    ''' Create column with the subtraction of column2 from column1'''
    df[subtraction_col] = (df[column1] - df[column2])
    return df


def df_column_to_int(df: pd, column: pd.column) -> pd:
    ''' Transform column data to integers '''
    df[column] = (df[column].astype('int'))
    return df


def add_ratio_column(
        df: pd,
        column_name: str,
        column2: pd.column,
        column1: pd.column
        ) -> pd:
    ''' Create column with the ratio of column2 / column1 '''
    df[column_name] = ((df[column2] / df[column1])-1)
    return df


def drop_column(df: pd, *args: pd.column) -> pd:
    ''' Drop columns from dataframe '''
    df.drop(list(args), axis=1, inplace=True)
    return df
