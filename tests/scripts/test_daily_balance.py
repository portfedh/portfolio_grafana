import unittest
import pandas as pd
import move_two_levels_up
from pandas import Timestamp
from scripts import daily_balance as db
from unittest import mock


class TestDailyBalance(unittest.TestCase):
    # Test class that inherits from  unittest.testcase
    # Gives access to testing capabilities.

    @mock.patch('scripts.daily_balance.pd.read_csv')
    def test_create_df(self, mock_read_csv):
        # Setup
        mock_read_csv.return_value = pd.DataFrame({
            'Date': ['2022-12-01', '2022-12-03', '2022-12-05'],
            'Tot_Acct': [111000, 222000, 333000],
            })
        # Call function
        actual = db.create_df('mock_file.csv')
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

    def test_daily_balance(self):
        # Setup df1
        data = {'Tot_Acct': [111000, 222000, 333000]}
        dates = pd.to_datetime(['2022-12-01', '2022-12-03', '2022-12-05'])
        df1 = pd.DataFrame(data, index=dates)
        df1 = df1.rename_axis('Date', axis=1)
        # Setup data_range
        d_range = pd.date_range('2022-12-01', periods=6)

        # Call function 1
        actual1 = db.create_daily_balance_df(
            df1, 'Tot_Acct', sum=True, range=d_range)
        # Call function 2
        actual2 = db.create_daily_balance_df(
            df1, 'Tot_Acct', sum=False, range=d_range)

        # Expected 1
        data = {'Tot_Acct': [111000, 111000, 333000, 333000, 666000, 666000]}
        dates = pd.date_range('2022-12-01', periods=6)
        expected1 = pd.DataFrame(data, index=dates)
        expected1 = expected1.rename_axis('Date', axis=1)
        expected1 = expected1.sort_index(axis=0, ascending=False)
        expected1
        # Expected 2
        data = {'Tot_Acct': [111000, 111000, 222000, 222000, 333000, 333000]}
        dates = pd.date_range('2022-12-01', periods=6)
        expected2 = pd.DataFrame(data, index=dates)
        expected2 = expected2.rename_axis('Date', axis=1)
        expected2 = expected2.sort_index(axis=0, ascending=False)

        # Tests
        pd.testing.assert_frame_equal(actual1, expected1, check_freq=False)
        pd.testing.assert_frame_equal(actual2, expected2, check_freq=False)
        # ADD TEST TO CHECK NA VALUES ARE TURNED TO ZEROS

    def test_add_df(self):
        # Setup
        df1 = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [4, 5, 6],
            })
        df2 = pd.DataFrame({
            'col_c': [7, 8, 9],
            'col_d': [10, 11, 12],
            })
        # Call function
        actual = db.concat_df(df1, df2, type=1)
        # Expectation
        expected = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [4, 5, 6],
            'col_c': [7, 8, 9],
            'col_d': [10, 11, 12],
            })
        expected
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_add_total_column(self):
        # Setup
        df1 = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [4, 5, 6],
            })
        # Call function
        actual = db.add_total_column_to_df(df1, 'col_tot')
        # Expectation
        expected = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [4, 5, 6],
            'col_tot': [5, 7, 9],
            })
        expected
        # Test
        pd.testing.assert_frame_equal(actual, expected)


if __name__ == "__main__":
    unittest.main()
