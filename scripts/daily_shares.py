# daily_shares.py
"""
Get the daily shares for each ticker in an account.

This module allows the user get the daily share quantities for each ticker
in one account.

The module contains the following functions:

- create_share_quantity_df(tickers):
    Returns an empty df with a date column and one column per ticker.

- create_daily_share_quantity(date_range, trade_history, ticker_list, df):
    Returns the number of shares per ticker for each day in date range.
"""

from datetime import datetime
import pandas as pd


def create_empty_share_quantity_df(tickers: list) -> 'pd':
    """
    Create an empty DataFrame with Date as index and each ticker as a column.

    Creates the DataFrame so total shares per day can be added by appending it.

        Parameters:
            tickers:
                - A list with the tickers to be added as columns.

        Returns:
            quantity_df:
                - Empty DataFrame.
                - 'Date' as index with datetime format.
                - Each ticker as column
    """
    # Create DataFrame columns
    column_list = tickers.copy()
    column_list.append('Date')
    # Create an empty DataFrame with column names
    quantity_df = pd.DataFrame(columns=column_list)
    # Convert 'Date' column from string to datetime
    date_column = pd.to_datetime(quantity_df['Date'])
    # Make the 'Date' Column the Index
    index_date_column = pd.DatetimeIndex(date_column.values)
    # Create DataFrame with new index and add 'Date' as column name
    quantity_df = quantity_df.set_index(index_date_column)
    quantity_df = quantity_df.rename_axis('Date', axis=1)
    # Drop original 'Date' Column
    quantity_df.drop('Date', axis=1, inplace=True)
    # Return the DataFrame
    return quantity_df


def create_daily_share_quantity(
        date_range: datetime,
        trade_history: 'pd',
        ticker_list: list,
        df: 'pd'
        ) -> 'pd':
    """
    Reads the trade history & returns a df with daily shares for every ticker.

    Takes a trade history df from a csv file and a date range.
    Outputs a df with daily share quantities per ticker for a date range.

        Parameters:
            date_range:
                - Dates to be analyzed.

            trade_history:
                - Data frame with trade history.

            ticker_list:
                - List of tickers in trade history DataFrame.

        Returns:
            df:
                - Empty df created using create_share_quantity_df().
                - Appended with one row per day with share totals per ticker.
    """
    # For loop: Go through every date:
    for date in date_range:
        # Temporary list
        values = []
        # For loop: Go through every ticker:
        for ticker in ticker_list:
            # Filter DataFrame by ticker
            filter_df = (
                trade_history[trade_history['Yfinance_Ticker'] == ticker])
            # Filter DataFrame up to date
            day_filter_df = filter_df.loc[:date]
            # Sum shares in DataFrame for that ticker
            total_shares = day_filter_df['Shares'].sum()
            # Append product to the temporary list
            values.append(total_shares)
        # Create dictionary with tickers and share values for given date
        new_row = dict(zip(ticker_list, values))
        # Create DataFrame from dictionary
        new_row_df = pd.DataFrame(new_row, index=[date])
        new_row_df = new_row_df.rename_axis('Date', axis=1)
        # Merge new row with DataFrame from create_share_quantity_df()
        df = pd.concat([new_row_df, df])
    df.sort_index(ascending=True, inplace=True)
    df = df.astype(int)
    return df
