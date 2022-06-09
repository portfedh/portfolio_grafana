import pandas as pd
from pyxirr import xirr


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
        Parameters:
        -----------
            file1: str, Input.
                String with contributions CSV 1 <path/filename.csv>.
            file2: str, Input.
                String with contributions CSV 2 <path/filename.csv>.
            col_name1: str, Input.
                String with column name for file 1 with contribution data.
            col_name2: str, Input.
                String with column name for file 2 with contribution data.
            sum_col_name: str, Output.
                String with column name for output DF with consolidated data.
        Returns:
        --------
            result: pd
                'Date' column as the index, in datetime format.
                 Column Values, with sum_col_name3 as column title, int.
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


def irr_monthly_balance_df(
        file1: 'pd',
        file2: 'pd',
        col_name1: str,
        col_name2: str,
        sum_col_name: str
        ) -> 'pd':
    """
    Creates a consolidated monthly account balance.

    From monthly account balance files for individual accounts.
    Takes two df and returns a new df with the addition of both values.
        Parameters:
        -----------
            file1: str, Input.
                Contributions CSV 1 <path/filename.csv>.
            file2: str, Input.
                Contributions CSV 2 <path/filename.csv>.
            col_name1: str, Input.
                Column name for file 1 with account balance data.
            col_name2: str, Input.
                Column name for file 2 with account balance data.
            sum_col_name: str, Output.
                Column name for output DF with consolidated data.
        Returns:
        --------
            result: pd
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


def calculate_xirr(
        acct_balance_df: 'pd',
        contributions_df: 'pd',
        balance_col_name: str,
        contrib_col_name: str
        ) -> float:
    """
    Calculates the XIRR from contributions and account balance dataframes.

    Uses consolidated contributions and consolidated account balances.
    Takes two df and returns the XIRR as a float number.
        Parameters:
        -----------
            acct_balance_file: df, Input.
                Consolidated account balances.
            contributions_file: df, Input.
                Consolidated contributions.
            balance_col_name: str, Input.
                Column name for acct_balance_file with account balance data.
            contrib_col_name: str, Input.
                Column name for contributions_file with contribution data.
        Returns:
        --------
            xirr_result: float
                XIRR value expressed as a decimal number.
                Must be multiplied by 100 to get as percentage.
    """
    # Get last value from account balances
    last_balance_value = acct_balance_df.iloc[-1:]
    # Rename column to match contributions df
    last_balance_value.rename(
        columns={balance_col_name: contrib_col_name},
        inplace=True)
    # Concatenate dataframes
    irr_df = pd.concat([contributions_df, last_balance_value])
    # Separate df into two lists
    pd_List1 = irr_df.index.tolist()
    pd_List2 = list(irr_df[contrib_col_name])
    # Pass lists into xirr function
    xirr_result = xirr(pd_List1, pd_List2)
    return xirr_result
