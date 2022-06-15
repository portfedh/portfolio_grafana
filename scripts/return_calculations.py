import pandas as pd


def returns(
        contributions: 'pd',
        balance: 'pd',
        col_contributions: str,
        col_balance: str,
        col_subtraction: str,
        col_ratio: str
        ) -> 'pd':
    """
    Calculates a simple return for the portfolio.

    Calculates Return$ = (Balance - Contributions).
    Calculates Return% = (Balance / Contributions) -1.
    Takes two df and returns a df with two columns.

        Parameters:
        -----------
            contributions: pd.
                Consolidated Daily Contributions.
            balance: pd.
                Consolidated Daily Account Balance.
            col_contributions: str.
                Column name from file 1.
            col_balance: str.
                Column name from file 2.
            col_subtraction: str.
                Column name for subtraction:
                    (col_name2 - col_name1).
            col_ratio: str.
                Column name for ratio:
                    (col_name2 / col_name1) - 1.

        Returns:
        --------
            returns: pd.
                Dataframe with 3 columns:
                    'Date' column as index in datetime format.
                    col_subtraction: int. Product of (balance - contributions).
                    col_ratio: float. Ratio of (balance / contributions)-1.
    """
    # Merge two files
    returns = contributions.merge(
        balance,
        left_index=True,
        right_index=True)
    # Add Column with the subtraction of column2 from column1
    returns[col_subtraction] = (
        returns[col_balance] - returns[col_contributions])
    # Save as Integer
    returns[col_subtraction] = (
        returns[col_subtraction].astype('int'))
    # Add Column with the ratio of column2 from column1
    returns[col_ratio] = (
        (returns[col_balance] / returns[col_contributions])-1)
    # Drop individual columns
    returns.drop(
        [col_contributions, col_balance],
        axis=1,
        inplace=True)
    # Return dataframe
    return returns
