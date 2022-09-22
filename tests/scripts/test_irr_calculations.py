# test_irr_calculations.py
"""
This test module will unit test all the functions in irr_calculations.py
"""

import unittest
import pandas as pd
from pandas import Timestamp
import move_two_levels_up
from scripts import irr_calculations as irr


class TestReturnCalculations(unittest.TestCase):
    # Test class that inherits from  unittest.testcase
    # Gives access to testing capabilities.

    def test_to_datetime_df(self):
        """
        Test if function makes 'Date' column the index with datetime format.

        Procedure:
            Setup:
                Create df with two columns: 'Date' and 'Values'.
            Call:
                Call the function with df.
            Expected:
                df with 'Date' as index.
                df with one column: 'Values'.
        """
        # Setup
        df1 = pd.DataFrame({
                'Date': ['29/01/21', '30/01/21', '31/01/21'],
                'Values': [99, 100, 101],
            })
        # Call function
        actual = irr.change_column_to_datetime(df1, 'Date')
        # Expectation
        data = {'Values': [99, 100, 101]}
        index = pd.date_range('29/01/21', periods=3)
        expected = pd.DataFrame(data, index=index)
        expected = expected.rename_axis('Date', axis=1)
        # Test
        pd.testing.assert_frame_equal(actual, expected, check_freq=False)

    def test_filter_df_by_column(self):
        """
        Test if function filters a df, keeping only the columns passed as args.

        Procedure:
            Setup:
                Create df1 with 4 columns: 'col_a', 'col_b', 'col_c', 'col_d'.
            Call:
                Call the function with df1.
                Select only two columns: 'col_a', 'col_c'.
            Expected:
                df1 showing two columns and their values: 'col_a', 'col_c'.
        """
        # Setup
        df1 = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [4, 5, 6],
            'col_c': [7, 8, 9],
            'col_d': [10, 11, 12],
            })
        # Call function
        actual = irr.filter_df_by_column(df1, ['col_a', 'col_c'])
        # Expectation
        expected = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_c': [7, 8, 9],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_invert_cf_df(self):
        """
        Test if function changes the values in a column by multiplying by (-1).

        Procedure:
            Setup:
                Create df1 with 2 columns: 'col_a', 'col_b'.
            Call:
                Call the function with df1.
                Select 'col_b' to invert that column. 
            Expected:
                df1 with 'col_a' with original values.
                df1 with 'col_b' with inverted values.
        """
        # Setup
        df1 = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [4, 5, 6],
            })
        # Call function
        actual = irr.invert_df_column_values(df1, 'col_b')
        # Expectation
        expected = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [-4, -5, -6],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_integers_df(self):
        """
        Test if function changes the values in df to integers.

        Procedure:
            Setup:
                Create df1 with 2 columns: 'col_a', 'col_b'.
                Set values for both columns as floats.
            Call:
                Call the function with df1.
                Select 'col_b' to change that column to integers.
            Expected:
                df1 with 'col_a' with values as floats.
                df1 with 'col_b' with values as integers.
        """
        # Setup
        df1 = pd.DataFrame({
            'col_a': [1.4, 2.5, 3.6],
            'col_b': [4.7, 5.8, 6.9],
            })
        # Call function
        actual = irr.change_column_to_integers(df1, 'col_b')

        # Expectation
        expected = pd.DataFrame({
            'col_a': [1.4, 2.5, 3.6],
            'col_b': [4, 5, 6],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_get_last_value(self):
        """
        Test if function filters the last row of a df.

        Procedure:
            Setup:
                Create df1 with 2 columns: 'col_a', 'col_b'.
                Set three values for both columns.
            Call:
                Call the function with df1.
                Reset index so it will match testing DataFrame.
            Expected:
                df1 with 'col_a' with only the last value.
                df1 with 'col_b' with only the last value.
        """
        # Setup
        df1 = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [4, 5, 6],
            })
        # Call function
        actual = irr.get_last_row_of_df(df1)
        actual = actual.reset_index(drop=True)
        # Expectation
        expected = pd.DataFrame({
            'col_a': [3],
            'col_b': [6],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_rename_column(self):
        """
        Test if function renames a column in a DataFrame.

        Procedure:
            Setup:
                Create df1 with 2 columns: 'col_a', 'col_b'.
            Call:
                Call the function with df1.
                Rename 'col_b' to 'col_new'.
            Expected:
                df1 with with 2 columns: 'col_a', 'col_new'.
                The values in 'col_b' == 'col_new'.
        """
        # Setup
        df1 = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [4, 5, 6],
            })
        # Call function
        actual = irr.rename_df_column(df1, 'col_b', 'col_new')
        # Expectation
        expected = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_new': [4, 5, 6],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_split_df(self):
        """
        Test if function saves dates and values in df as two  lists.

        Procedure:
            Setup:
                Create df1 with 2 columns: 'Date', 'Values'.
                Make 'Date'the index in datetime format.
            Call:
                Call the function with df1 and 'Values' column.
            Expected:
                'dates_actual': A  list with the dates from df1.
                'values_actual': A list with the values from df1.
        """
        # Setup
        data = {'Values': [99, 100, 101]}
        index = pd.date_range('29/01/21', periods=3)
        df1 = pd.DataFrame(data, index=index)
        df1 = df1.rename_axis('Date', axis=1)
        # Call function
        dates_actual, values_actual = irr.split_df_into_two_lists(df1, 'Values')
        # Expectation
        dates_expected = [
            Timestamp('2021-01-29 00:00:00'),
            Timestamp('2021-01-30 00:00:00'),
            Timestamp('2021-01-31 00:00:00')
            ]
        values_expected = [99, 100, 101]
        # Test
        self.assertEqual(dates_actual, dates_expected)
        self.assertEqual(values_actual, values_expected)


if __name__ == "__main__":
    unittest.main()
