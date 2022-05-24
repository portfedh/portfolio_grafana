import pandas as pd
import set_analysis_dates


def create_df(file_name: str) -> 'pd':
    """Create a dataframe from CSV.
    'Date' is the index in datetime format,
    values are integers or floats."""
    df = pd.read_csv(file_name)
    # Create list from 'Date' column
    datetime_list = pd.to_datetime(
        df['Date'], dayfirst=True)
    # Make 'Date' column an index object
    datetime_list = pd.DatetimeIndex(datetime_list.values)
    # Append new 'Date' column to dataframe, as index
    df = df.set_index(datetime_list)
    # Add 'Date' label to index column
    df = df.rename_axis('Date', axis=1)
    # Drop original 'Date' column
    df.drop('Date', axis=1, inplace=True)
    return df


def daily_balance(df: 'pd', column_name: str, sum: bool) -> 'pd':
    """Create dataframe with dailiy balances.
    Requires dataframe from 'create_df function' as input.
    'column_name' must equal the name of the column in input file.
    'sum'=True will add values up to that date.
    'sum'=False it append the latest value
    'Date' is the index in datetime format,
    values are displayed as integers."""
    # Create output dataframe
    daily_df = pd.DataFrame(columns=[column_name])
    for date in set_analysis_dates.date_range:
        # Filter dataframe up to date
        filtered_blance_df = df.loc[:date]
        if sum is True:
            # Get the sum of values to date
            value = filtered_blance_df[column_name].sum()
        else:
            # Get last value
            value = filtered_blance_df[column_name].iloc[-1]
        # Create dictionary with value
        new_dic_row = {column_name: value}
        # Create dataframe from dictionary
        new_row_df = pd.DataFrame(new_dic_row, index=[date])
        # Merge with output dataframe
        daily_df = pd.concat(
            [new_row_df, daily_df])
    # Set column from string to integer
    daily_df[column_name] = (
        daily_df[column_name].astype(int))
    # Add 'Date' label to the index column
    daily_df = daily_df.rename_axis(
        'Date', axis=1)
    return daily_df


def consolidate(file_name_1: str, file_name_2: str, col_name: str) -> 'pd':
    """Create dataframe from multiple CSV files.
    Requires CSV files from 'daily_balance' function as input.
    'col_name' is the name of the column adding the values.
    'Date' column  is the index, in datetime format,
    values are displayed as integers."""
    # Get balances from CSVs
    df_1 = pd.read_csv(file_name_1)
    df_2 = pd.read_csv(file_name_2)
    # Merge dataframes
    df_total = df_1.copy()
    column_name = df_2.columns[1]
    df_total[column_name] = df_2[[column_name]].copy()
    # Add Total Values
    df_total[col_name] = (
        df_total[df_total.columns[1]] + df_total[df_total.columns[2]])
    # Drop other columns
    df_total.drop(
        columns=[df_total.columns[1], df_total.columns[2]], inplace=True)
    return df_total
