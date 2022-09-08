import unittest
import pandas as pd
import move_two_levels_up
from pandas import Timestamp
from scripts import daily_shares as ds


class TestReturnCalculations(unittest.TestCase):
    # Test class that inherits from  unittest.testacse
    # Gives access to testing capabilities.

    def test_create_empty_share_quantity_df(self):
        # Setup
        ticker_list = ["VOO", "VGK", "VPL"]

        # Call function
        actual = ds.create_empty_share_quantity_df(ticker_list)

        # Expectation
        # Create ticker list
        expected_list = ["Date", "VOO", "VGK", "VPL"]
        expected = pd.DataFrame(columns=expected_list)
        # Convert 'Date' column from string to datetime
        date_column = pd.to_datetime(expected['Date'])
        # Make the 'Date' Column the Index
        index_date_column = pd.DatetimeIndex(date_column.values)
        # Create dataframe with new index and add 'Date' as column name
        expected = expected.set_index(index_date_column)
        expected = expected.rename_axis('Date', axis=1)
        # Drop original 'Date' Column
        expected.drop('Date', axis=1, inplace=True)

        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_create_daily_share_quantity_df(self):
        # Setup
        date_range1 = pd.date_range(start="2022-12-01", end="2022-12-06")
        dates1 = [
            Timestamp('2022-12-01 00:00:00'),
            Timestamp('2022-12-03 00:00:00'),
            Timestamp('2022-12-05 00:00:00'),
            ]
        df1 = pd.DataFrame({
            'Ticker': ['VOO', 'VOO', 'VOO'],
            'Yfinance_Ticker': ['VOO.MX', 'VOO.MX', 'VOO.MX'],
            'Trade': ['Buy', 'Buy', 'Sell'],
            'Shares': [10, 5, -3],
            }, index=dates1)
        df1 = df1.rename_axis('Date', axis=1)
        yftickers = list(df1['Yfinance_Ticker'].unique())
        df2 = ds.create_empty_share_quantity_df(yftickers)

        # Call function
        actual = ds.create_daily_share_quantity(
            date_range=date_range1,
            trade_history=df1,
            ticker_list=yftickers,
            df=df2)

        # Expectation
        dates_expected = pd.date_range('2022-12-01', periods=6)
        expected = pd.DataFrame({
            'VOO.MX': [10, 10, 15, 15, 12, 12],
            }, index=dates_expected)
        expected = expected.rename_axis('Date', axis=1)

        # Test
        pd.testing.assert_frame_equal(actual, expected, check_freq=False)


if __name__ == "__main__":
    unittest.main()
