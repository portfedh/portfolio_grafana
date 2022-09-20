import unittest
import pandas as pd
import move_two_levels_up
from scripts import return_calculations as rt


class TestReturnCalculations(unittest.TestCase):
    # Test class that inherits from  unittest.testcase
    # Gives access to testing capabilities.

    def test_subtract_column(self):
        """
        Test if function appends a column with subtraction of 2 columns in df.

        Procedure:
            Setup:
                Create df1 with two columns: 'col_a' and 'col_b'.
            Call:
                Call the function with df1.
                Choose the columns to be subtracted: 'col_a' and 'col_b'.
                Choose the name of the column with the result: 'col_c'.
            Expected:
                DataFrame with three columns: 'col_a', 'col_b', 'col_c'.
                Values in 'col_c' are the subtraction of (col_a)-(col_b).
        """
        # Setup
        df1 = pd.DataFrame({
                'col_a': [50, 50, 50],
                'col_b': [30, 30, 30],
            })
        # Call function
        actual = rt.subtract_columns_in_df(df1, 'col_a', 'col_b', 'col_c')
        # Expectation
        expected = pd.DataFrame({
                'col_a': [50, 50, 50],
                'col_b': [30, 30, 30],
                'col_c': [20, 20, 20],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_add_ratio_column(self):
        """
        Test if function appends a column with ratio of 2 columns in df.

        Procedure:
            Setup:
                Create df1 with two columns: 'col_a' and 'col_b'.
            Call:
                Call the function with df1.
                Choose the columns to be divided: 'col_a' and 'col_b'.
                Choose the name of the column with the result: 'col_c'.
            Expected:
                DataFrame with three columns: 'col_a', 'col_b', 'col_c'.
                Values in 'col_c' are the ratio of ((col_a)/(col_b))*(-1).
        """
        # Setup
        df1 = pd.DataFrame({
                'col_a': [100, 200, 400],
                'col_b': [200, 400, 800],
            })
        # Call function
        actual = rt.add_ratio_column_in_df(
            df=df1, column_name='col_c', column2='col_a', column1='col_b'
            )
        # Expectation
        expected = pd.DataFrame({
                'col_a': [100, 200, 400],
                'col_b': [200, 400, 800],
                'col_c': [-0.5, -0.5, -0.5],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_drop_column(self):
        """
        Test if function drops a column in a DataFrame.

        Procedure:
            Setup:
                Create df1 with three columns: 'col_a','col_b','col_c'.
            Call:
                Call the function with df1.
                Choose the columns to be dropped: 'col_c'.
            Expected:
                DataFrame with three columns: 'col_a', 'col_b'.
                'col_c' has been dropped.
        """
        # Setup
        df1 = pd.DataFrame({
                'col_a': [100, 200, 300],
                'col_b': [400, 500, 600],
                'col_c': [700, 800, 900],
            })
        # Call function
        actual = rt.drop_column(df1, 'col_c')
        # Expectation
        expected = pd.DataFrame({
                'col_a': [100, 200, 300],
                'col_b': [400, 500, 600],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)


if __name__ == "__main__":
    unittest.main()
