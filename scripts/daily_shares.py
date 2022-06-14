from datetime import datetime
import pandas as pd


def create_share_quantity_df(tickers: list) -> 'pd':
    """
    Create an empty dataframe with Data as index and each ticker as a column.

    Creates the dataframe so data can be added by appending rows.
        Parameters:
        -----------
            tickers: list, Input.
                Pass a list with the tickers to be added
        Returns:
        --------
            quantity_df: pdf.
                Empty dataframe.
                'Date' as index with datetime format.
                Each ticker as column
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
        daily_shares: 'pd'  # Dataframe to append
        ) -> 'pd':
    """
    Takes trade history and outputs daily shares for every ticker.

    Takes a trade history df and a date range.
    It outputs a df with daily share quantities per ticker.
    Using onw row for every day within the given date range.
        Parameters:
        -----------
            date_range: datetime, input.
                Dates to be analysed.
            trade_history: pd, input.
                Dataframe with trade history.
            ticker_list: list.
                list of tickers in trade history dataframe.
        Returns:
        --------
            daily_shares: pd.
                Dataframe with:
                    - Share values per ticker.
                    - For every date in daterange.
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
        # Append the original dataframe with this new row
        # shares = shares.append(pd.DataFrame(new_row, index=[date]))
        # Merge new row with output dataframe
        daily_shares = pd.concat([new_row_df, daily_shares])
    return daily_shares
