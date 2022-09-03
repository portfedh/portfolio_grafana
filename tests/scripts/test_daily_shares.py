# Run using:
# $ python3 -m unittest -v tests/scripts/test_return_calculations.py

import unittest
import pandas as pd
import move_two_levels_up
from scripts import daily_shares as ds


class TestReturnCalculations(unittest.TestCase):
    # Test class that inherits from  unittest.testacse
    # Gives access to testing capabilities.

    def test_create_share_quantity_df(self):
        # Setup
        ticker_list = ["VOO", "VGK", "VPL"]

        # Call function
        actual = ds.create_share_quantity_df(ticker_list)

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


if __name__ == "__main__":
    unittest.main()
