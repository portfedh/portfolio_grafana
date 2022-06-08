import pandas as pd


def returns(
        file1: 'pd',
        file2: 'pd',
        col_name1: str,
        col_name2: str,
        col_name3: str,
        col_name4: str
        ) -> 'pd':
    """
    Takes two df and returns a df with two columns.

    The column will be the subtraction and
        Parameters:
        -----------
            file1: pd.
                Dataframe 1.
            file2: pd.
                Dataframe 2.
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
    file1 = file1.merge(file2, left_index=True, right_index=True)
    # Add Column with the subtraction of column2 from column1
    file1[col_name3] = (file1[col_name2] - file1[col_name1])
    # Save as Integer
    file1[col_name3] = (file1[col_name3].astype('int'))
    # Add Column with the ratio of column2 from column1
    file1[col_name4] = ((file1[col_name2] / file1[col_name1])-1)
    # Drop individual columns
    file1.drop([col_name1, col_name2], axis=1, inplace=True)
    # Return dataframe
    return file1
