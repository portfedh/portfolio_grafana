import unittest
import pandas as pd
import move_two_levels_up
from pandas import Timestamp
from scripts import daily_balance as db
from unittest import mock


class TestReturnCalculations(unittest.TestCase):
    # Test class that inherits from  unittest.testacse
    # Gives access to testing capabilities.

    @mock.patch('scripts.daily_balance.pd.read_csv')
    def test_create_df(self, mock_read_csv):
        
        # Setup
        mock_read_csv.return_value = pd.DataFrame({
            'Date': ['2022-12-01', '2022-12-03', '2022-12-05'],
            'Tot_Acct': [111000, 222000, 333000],
            })

        # Call function
        actual = db.create_df('students_mock.csv')

        # Expected
        dates = [
            Timestamp('2022-12-01 00:00:00'),
            Timestamp('2022-12-03 00:00:00'),
            Timestamp('2022-12-05 00:00:00'),
            ]
        df = pd.DataFrame({
            'Tot_Acct': [111000, 222000, 333000],
            }, index=dates)
        expected = df.rename_axis('Date', axis=1)

        # Test
        pd.testing.assert_frame_equal(actual, expected, check_exact=True)


if __name__ == "__main__":
    unittest.main()
