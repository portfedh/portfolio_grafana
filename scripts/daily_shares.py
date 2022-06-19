# daily_shares.py
"""Gets the daily shares for each ticker in an account.

This module allows the user get daily share amounts for each ticker
in one account.

The module contains the following functions:

- create_share_quantity_df(tickers):
    Returns an empty df with a date column and one column per ticker.

- create_daily_share_quantity(date_range, trade_history, ticker_list, df):
    Returns the number of shares per ticker for each day in date range.
"""

from datetime import datetime
import pandas as pd


def create_share_quantity_df(tickers: list) -> 'pd':
    """
    Create an empty dataframe with Date as index and each ticker as a column.

    Creates the dataframe so total shares per day can be added by appending it.

        Parameters:
            tickers:
                - A list with the tickers to be added as columns.

        Returns:
            quantity_df:
                - Empty dataframe.
                - 'Date' as index with datetime format.
                - Each ticker as column
    """
    # Create dataframe columns
    column_list = tickers.copy()
    column_list.append('Date')
    # Create an empty dataframe with column names
    quantity_df = pd.DataFrame(columns=column_list)
    # Convert 'Date' column from string to datetime
    date_column = pd.to_datetime(quantity_df['Date'])
    # Make the 'Date' Column the Index
    index_date_column = pd.DatetimeIndex(date_column.values)
    # Create dataframe with new index and add 'Date' as column name
    quantity_df = quantity_df.set_index(index_date_column)
    quantity_df = quantity_df.rename_axis('Date', axis=1)
    # Drop original 'Date' Column
    quantity_df.drop('Date', axis=1, inplace=True)
    # Return the dataframe
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
                - Dates to be analysed.

            trade_history:
                - Data frame with trade history.

            ticker_list:
                - List of tickers in trade history dataframe.

        Returns:
            df:
                - Empty df creaded using create_share_quantity_df().
                - Appended with one row per day with share totals per ticker.
    """
    dates = date_range
    # For loop: Go through every date:
    for date in dates:
        # Temporary list
        values = []
        # For loop: Go through every ticker:
        for ticker in ticker_list:
            # Filter dataframe by ticker
            filter_df = (
                trade_history[trade_history['Yfinance_Ticker'] == ticker])
            # Filter dataframe up to date
            day_filter_df = filter_df.loc[:date]
            # Sum shares in dataframe for that ticker
            total_shares = day_filter_df['Shares'].sum()
            # Append product to the temporary list
            values.append(total_shares)
        # Create dictionary with tickers and share values for given date
        new_row = dict(zip(ticker_list, values))
        # Create dataframe from dictionary
        new_row_df = pd.DataFrame(new_row, index=[date])
        # Merge new row with dataframe from create_share_quantity_df()
        df = pd.concat([new_row_df, df])
    return df
