# irr_calculations.py
"""Calculate the IRR of the portfolio.

Uses consolidated contributions and the last value in
the consolidated account balance.

The module contains the following functions:

- irr_contributions_df(file1, file2, col_name1, col_name2, sum_col_name):
    Returns a consolidated constibutions df from two accounts.

- irr_monthly_balance_df( file1, file2, col_name1, col_name2, sum_col_name):
    Returns a consolidated monthly account balance from two accounts.

- calculate_xirr( acct_balance_df, contributions_df, bal_column, cont_column):
    Returns the xirr of the portfolio using contributions and account balances.
"""

import pandas as pd
from pyxirr import xirr


# ### New Functions ##########################################################
# Will Substitute irr_contributions()
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
# ### End New Functions ######################################################


# ### To Delete ##############################################################
def irr_contributions_df(
        file1: str,
        file2: str,
        col_name1: str,
        col_name2: str,
        sum_col_name: str
        ) -> 'pd':
    """
    Creates a consolidated contributions dataframe.

    From contribution files for individual accounts.
    Takes two df and returns a new df with the addition of both values.
        - Contributions are shown as negative numbers (-).
        - Distributions are shown as positive numbers (+).

        Parameters:
            file1:
                String with contributions csv file 1 <path/filename.csv>.

            file2:
                String with contributions csv file 2 <path/filename.csv>.

            col_name1:
                String with column name for file 1 with contribution data.

            col_name2:
                String with column name for file 2 with contribution data.

            sum_col_name:
                String with column name for output df with consolidated data.

        Returns:
            result:
                'Date' column as the index, in datetime format.
                Column values, with sum_col_name as column title.
    """
    # Import data
    df_1 = pd.read_csv(file1)
    df_2 = pd.read_csv(file2)
    # Join dataframes
    result = pd.concat([df_1, df_2])
    # Substitute NA values with zeros
    result = result.fillna(0)
    # Add contributions of both accounts
    result[sum_col_name] = (
        result[col_name1] + result[col_name2])
    # Drop columns
    result.drop([col_name1, col_name2], axis=1, inplace=True)
    # Invert values from (+) to (-)
    result[sum_col_name] = result[sum_col_name]*-1
    result[sum_col_name] = result[sum_col_name].astype('int')
    # Set 'Date' column as DateTime and set to index
    datetime_date = pd.to_datetime(result['Date'], dayfirst=True)
    datetime_index_trades = pd.DatetimeIndex(datetime_date.values)
    result = result.set_index(datetime_index_trades)
    result = result.rename_axis('Date', axis=1)
    result.drop('Date', axis=1, inplace=True)
    # Sort values by date in ascending order
    result.sort_index()
    # Return dataframe
    return result
# ### End To Delete ##########################################################

# ### New Functions ##########################################################
# Will Substitute irr_monthly_balance_df()


# Very similar to concat_df but with axis=1 and without read CSV
def merge_df(*args: pd):
    """Merge unlimited dataframes"""
    list = []
    for x in args:
        list.append(x)
    # Concatenate
    result = pd.concat(list, axis=1)
    return result
# ### End New Functions ######################################################


# ### To Delete ##############################################################
def irr_monthly_balance_df(
        file1: 'pd',
        file2: 'pd',
        col_name1: str,
        col_name2: str,
        sum_col_name: str
        ) -> 'pd':
    """
    Returns a consolidated monthly account balance from two accounts.

    Uses monthly account balance dataframes from two accounts.
    Returns a new df with the addition of both values.

        Parameters:
            file1:
                Account balance csv file 1 <path/filename.csv>.

            file2:
                Account balance csv file 2 <path/filename.csv>.

            col_name1:
                Column name for file 1 with account balance data.

            col_name2:
                Column name for file 2 with account balance data.

            sum_col_name:
                Column name for output with consolidated data.

        Returns:
            result:
                'Date' column as the index, in datetime format.
                 Column Values, with sum_col_name as column title, int.
    """
    # Merge two files
    file1 = file1.merge(file2, left_index=True, right_index=True)
    # Add Column with the sum of both columns
    file1[sum_col_name] = (file1[col_name1] + file1[col_name2])
    # Save as Integer
    file1[sum_col_name] = (file1[sum_col_name].astype('int'))
    # Drop individual columns
    file1.drop([col_name1, col_name2], axis=1, inplace=True)
    # Return dataframe
    return file1
# ### End To Delete ##########################################################


def calculate_xirr(
        acct_balance_df: 'pd',
        contributions_df: 'pd',
        bal_column: str,
        cont_column: str
        ) -> float:
    """
    Calculates the XIRR of a portfolio from contributions and account balance.

    Uses consolidated contributions and consolidated account balances.
    Returns the XIRR as a float number.

        Parameters:
            acct_balance_df:
                - Consolidated account balances df.

            contributions_df: Input.
                - Consolidated contributions df.

            bal_column:
                - Column name containing values in acct_balance_df.

            cont_column: Input.
                - Column name containing values in contributions_df.

        Returns:
            xirr_result:
                - XIRR value expressed as a decimal number.
                - Must be multiplied by 100 to expess as percentage.
    """
    # Get last value from account balances
    last_balance_value = acct_balance_df.copy(deep=True)
    last_balance_value = last_balance_value.iloc[-1:]
    # Rename column to match contributions df
    last_balance_value.rename(
        columns={bal_column: cont_column},
        inplace=True)
    # Concatenate dataframes
    irr_df = pd.concat([contributions_df, last_balance_value])
    # Separate df into two lists
    pd_List1 = irr_df.index.tolist()
    pd_List2 = list(irr_df[cont_column])
    # Pass lists into xirr function
    xirr_result = xirr(pd_List1, pd_List2)
    return xirr_result
