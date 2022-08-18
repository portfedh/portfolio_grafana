# return_calculations.py
"""Calculates a simple return for the portfolio in $ and % amounts.

The module contains the following functions:

- returns(contributions, balance, col_contrb, col_balance, col_sub, col_ratio):
    Calculates a simple return for the portfolio in $ ammount and % ammount.
"""

import pandas as pd


#  To Delete #################################################################
def returns(
        contributions: 'pd',
        balance: 'pd',
        col_contrb: str,
        col_balance: str,
        col_sub: str,
        col_ratio: str
        ) -> 'pd':
    """
    Calculates a simple return for the portfolio in $ and % amounts.

    Calculations are as follows:
        Return $ = (Balance - Contributions).
        Return % = (Balance / Contributions) - 1.

        Parameters:
            contributions:
                - Consolidated daily contributions dataframe.

            balance:
                - Consolidated daily account balance dataframe.

            col_contrb:
                - Column name from file 1 with values.

            col_balance:
                - Column name from file 2 with values.

            col_sub:
                - Column name for subtraction results:
                    (col_name2 - col_name1).

            col_ratio:
                - Column name for ratio results:
                    (col_name2 / col_name1) - 1.

        Returns:
            returns:
                - Dataframe with 3 columns:
                    'Date' column as index in datetime format.
                    col_sub: int. Product of (balance - contributions).
                    col_ratio: float. Ratio of (balance / contributions)-1.
    """
    # Merge two files
    returns = contributions.merge(
        balance,
        left_index=True,
        right_index=True)
    # Add Column with the subtraction of column2 from column1
    returns[col_sub] = (
        returns[col_balance] - returns[col_contrb])
    # Save as Integer
    returns[col_sub] = (
        returns[col_sub].astype('int'))
    # Add Column with the ratio of column2 from column1
    returns[col_ratio] = (
        (returns[col_balance] / returns[col_contrb])-1)
    # Drop individual columns
    returns.drop(
        [col_contrb, col_balance],
        axis=1,
        inplace=True)
    # Return dataframe
    return returns
#  End To Delete #############################################################


#  New Functions #############################################################

def merge_df(dataframe1, dataframe2):
    ''' Merge dataframe2 into dataframe1'''
    merged_df = dataframe1.merge(
        dataframe2, left_index=True, right_index=True)
    return merged_df


def subtract_column(df, column1, column2, subtraction_col):
    ''' Create column with the subtraction of column2 from column1'''
    df[subtraction_col] = (df[column1] - df[column2])
    return df


def df_column_to_int(df, column):
    ''' Transform column data to Integers '''
    df[column] = (df[column].astype('int'))
    return df


def add_ratio_column(df, column_name, column2, column1):
    ''' Create column with the ratio of column2 / column1 '''
    df[column_name] = ((df[column2] / df[column1])-1)
    return df


def drop_column(df, *args):
    ''' Drop columns from dataframe '''
    df.drop(list(args), axis=1, inplace=True)
    return df

#  End New Functions #########################################################
