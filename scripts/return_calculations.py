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
            file1: pd.
                Consolidated Daily Contributions.
            file2: pd.
                Consolidated Daily Account Balance.
            col_name1: str.
                Column name from file 1.
            col_name2: str.
                Column name from file 2.
            col_name3: str.
                Column name for subtraction:
                    (col_name2 - col_name1).
            col_name4: str.
                Column name for ratio:
                    (col_name2 / col_name1) - 1.

        Returns:
        --------
            file1: pd.
                Dataframe with 3 columns:
                    'Date' column as index in datetime format.
                    col_name3: int. Column with product of column2 - column1.
                    col_name4: float. Column with ratio (column2 / column1)-1.
    """
    # Merge two files
    contributions = contributions.merge(
        balance,
        left_index=True,
        right_index=True)
    # Add Column with the subtraction of column2 from column1
    contributions[col_subtraction] = (
        contributions[col_balance] - contributions[col_contributions])
    # Save as Integer
    contributions[col_subtraction] = (
        contributions[col_subtraction].astype('int'))
    # Add Column with the ratio of column2 from column1
    contributions[col_ratio] = (
        (contributions[col_balance] / contributions[col_contributions])-1)
    # Drop individual columns
    contributions.drop(
        [col_contributions, col_balance],
        axis=1,
        inplace=True)
    # Return dataframe
    return contributions
