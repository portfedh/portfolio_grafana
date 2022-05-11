import pandas as pd
import datetime as dt
import analysis_dates

def create_balance_df(file_name: str) -> 'pd':
    """Create a dataframe from imported CSV file.
    'Date' column  is the index, in datetime format,
    values are displayed as floats."""
    balance_df = pd.read_csv(file_name)
    # Create list from 'Date' column 
    datetime_index_trades = pd.to_datetime(balance_df['Date'])
    # Make 'Date' column an index object
    datetime_index_trades = pd.DatetimeIndex(datetime_index_trades.values)
    # Append new 'Date' column to dataframe, as index
    balance_df = balance_df.set_index(datetime_index_trades)
    # Add 'Date' label to index column
    balance_df = balance_df.rename_axis('Date', axis=1)
    # Drop original 'Date' column
    balance_df.drop('Date',axis=1,inplace=True)
    return balance_df

def create_daily_balance_df(balance_df:'pd', column_name:str) -> 'pd':
    """Create dataframe with dailiy balances, 
    requires the return dataframe from 'create_balance_df function' as input.
    'Date' column  is the index, in datetime format,
    values are displayed as integers."""
    # Create output dataframe
    daily_balance_df = pd.DataFrame(columns = [column_name])
    for date in analysis_dates.date_range:
        # Filter dataframe up to date
        filtered_blance_df = balance_df.loc[:date]
        # Get the last balance value
        current_balance = filtered_blance_df[column_name].iloc[-1]
        # Create dictionary with value
        new_row_dic =  {column_name:current_balance}
        # Create dataframe from dictionary
        new_row_df = pd.DataFrame(new_row_dic, index=[date])
        # Merge with output dataframe
        daily_balance_df = pd.concat([new_row_df, daily_balance_df])
    # Convert column from string to integer
    daily_balance_df[column_name] = daily_balance_df[column_name].astype(int)
    # Add 'Date' label to the index column
    daily_balance_df = daily_balance_df.rename_axis('Date', axis=1)
    return daily_balance_df

if __name__ == "__main__":
    pass