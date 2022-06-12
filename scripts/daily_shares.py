from datetime import datetime
import pandas as pd


def create_share_quantity_df(tickers: list) -> 'pd':
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
                                df: 'pd',  # df con trade history
                                ticker_list: list,  # lista de tickers
                                shares: 'pd'  # List to append
                                ) -> 'pd':

    dates = date_range
    # For loop: Go through every date:
    for date in dates:
        # Temporary list
        values = []
        # For loop: Go through every ticker:
        for ticker in ticker_list:
            # Filter dataframe by ticker
            filter_df = df[df['Ticker'] == ticker]
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
        shares = pd.concat([new_row_df, shares])
    return shares
