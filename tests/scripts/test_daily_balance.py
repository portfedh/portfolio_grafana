# test_daily_balance.py
"""
This test module will unit test all the functions in daily_balance.py
"""

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
        """
        Test that function sets 'Date' column as index
        and dates are in datetime format.

        Procedure:
            Setup:
                Create df with dates and values.
                Dates are str, values are int.
            Call:
                Pass mock file to function.
            Expected:
                df with dates and values.
                Dates are datetime, values are int.
        """
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

    def test_create_daily_balance_df(self):
        """
        Test that function:
            Creates a df with a row for every date in a date range.
            Displays the last data value for a date in a date range.
            Displays the cumulative sum value for every date in a date range.

        Procedure:
            Setup:
                Create df with dates and values.
                Dates are datetime, values are int.
                'Date' column is the index.
                'Tot_Acct' are the values to be tested.
                Define a date range.
            Call 1:
                Call function with the df from setup.
                Select sum=true to get cumulative total.
            Call 2:
                Call function with setup df.
                Select sum=false to get last value.
            Expected1:
                DataFrame with 'Date' column as the index.
                Dates are datetime, values are int.
                Values are the cumulative total of 'Tot_Acct'.
            Expected2:
                DataFrame with 'Date' column as the index.
                Dates are datetime, values are int.
                Values are the last value of 'Tot_Acct'.
        """
        # Setup df1
        data = {'Tot_Acct': [111000, 222000, 333000]}
        dates = pd.to_datetime(['2022-12-01', '2022-12-03', '2022-12-05'])
        df1 = pd.DataFrame(data, index=dates)
        df1 = df1.rename_axis('Date', axis=1)
        # Setup date_range
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
        # Expected 2
        data = {'Tot_Acct': [111000, 111000, 222000, 222000, 333000, 333000]}
        dates = pd.date_range('2022-12-01', periods=6)
        expected2 = pd.DataFrame(data, index=dates)
        expected2 = expected2.rename_axis('Date', axis=1)
        expected2 = expected2.sort_index(axis=0, ascending=False)
        # Tests
        pd.testing.assert_frame_equal(actual1, expected1, check_freq=False)
        pd.testing.assert_frame_equal(actual2, expected2, check_freq=False)
        # ADD ANOTHER TEST TO CHECK NA VALUES ARE TURNED TO ZEROS
        # SEPARATE CUMULATIVE SUM AND LAST VALUE INTO TWO TESTS

    def test_concat_df(self):
        """
        Test that function adds columns to DataFrame.

        Procedure:
            Setup:
                Create df1 with two columns and values.
                Create df2 with two columns and more values.
            Call:
                Call the function with df1 and df2.
                Select type=1 to concatenate columns.
            Expected:
                df1 with columns of df2 appended to the right.
        """
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
        # Test
        pd.testing.assert_frame_equal(actual, expected)
        # ADD ANOTHER TEST WHERE TYPE=0 FOR ROW CONCAT

    def test_add_total_column_to_df(self):
        """
        Test that function appends a columns adding row totals to DataFrame.

        Procedure:
            Setup:
                Create df1 with two columns and values.
            Call:
                Call the function with df1.
                Name 'col_tot' the column that will add row totals.
            Expected:
                df1 with new column 'col_tot' appended to the right.
                Values of 'col_tot' are the sum of 'col_a' and 'col_b'.
        """
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
