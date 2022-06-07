import pandas as pd
from pyxirr import xirr


def irr_contributions_df(
        file1: str,
        file2: str,
        col_name1: str,
        col_name2: str,
        col_name3: str
        ) -> 'pd':
    # Import data
    df_1 = pd.read_csv(file1)
    df_2 = pd.read_csv(file2)
    # Join dataframes
    result = pd.concat([df_1, df_2])
    # Substitute NA values with zeros
    result = result.fillna(0)
    # Add contributions of both accounts
    result[col_name3] = (
        result[col_name1] + result[col_name2])
    # Drop columns
    result.drop([col_name1, col_name2], axis=1, inplace=True)
    # Invert values from (+) to (-)
    result[col_name3] = result[col_name3]*-1
    result[col_name3] = result[col_name3].astype('int')
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
        col_name3: str
        ) -> 'pd':
    # Merge two files
    file1 = file1.merge(file2, left_index=True, right_index=True)
    # Add Column with the sum of both columns
    file1[col_name3] = (file1[col_name1] + file1[col_name2])
    # Save as Integer
    file1[col_name3] = (file1[col_name3].astype('int'))
    # Drop individual columns
    file1.drop([col_name1, col_name2], axis=1, inplace=True)
    # Return dataframe
    return file1


def calculate_xirr(
        file1: 'pd',
        file2: 'pd',
        col_name1: str,
        col_name2: str
        ) -> float:
    # Get last value
    last = file1.copy(deep=True)
    last = last.iloc[-1:]
    # Rename column to match other DF
    last.rename(
        columns={col_name1: col_name2},
        inplace=True)
    # Concatenate dataframes
    irr_df = pd.concat([file2, last])
    pdToList = irr_df.index.tolist()
    pdToList2 = list(irr_df[col_name2])
    result = xirr(pdToList, pdToList2)
    return result
