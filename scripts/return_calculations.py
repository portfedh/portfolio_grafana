# return_calculations.py

"""
This module contains functions used to calculate
the return for the portfolio in $ and % amounts.

The module contains the following functions:

- subtract_column(df, column1, column2, subtraction_col):
    Add a column to a DataFrame with the subtraction of column2 from column1.

- add_ratio_column(df, column_name, column2, column1):
    Add a column to a DataFrame with the ratio of column2 / column1.

- drop_column(df: pd, *args: pd.column) -> pd:
    Drop the columns passed as *args from DataFrame.
"""

import pandas as pd


def subtract_columns_in_df(
        df: pd,
        column1: str,
        column2: str,
        subtraction_col: str,
        ) -> pd:
    """
    Add a column to a DataFrame with the subtraction of column2 from column1.

        Parameters:
            df: Input DataFrame.
            column1: Name of column with minuend.
            column2: Name of column with subtrahend.
            subtraction_col: Name of the column with subtraction results.
        Returns:
            df: Output DataFrame with subtraction column appended.
    """
    df[subtraction_col] = (df[column1] - df[column2])
    return df


def add_ratio_column_in_df(
        df: pd,
        column_name: str,
        column2: pd,
        column1: pd
        ) -> pd:
    """
    Add a column to a DataFrame with the ratio of column2 / column1.

        Parameters:
            df: Input DataFrame.
            column_name: Name of the column with ratio results.
            column2: Column name of numerator.
            column1: Column name of denominator.
        Returns:
            df: Output DataFrame with ratio column appended.
    """
    df[column_name] = ((df[column2] / df[column1])-1)
    return df


def drop_column(df: pd, *args: pd) -> pd:
    """
    Drop the columns passed as *args from DataFrame.
    
        Parameters:
            df: Input DataFrame
            *args: Column names to drop (unlimited number).
        Returns:
            df: Output DataFrame without dropped columns. 
    """
    df.drop(list(args), axis=1, inplace=True)
    return df
