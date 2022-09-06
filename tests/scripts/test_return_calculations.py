# Run using:
# $ python3 -m unittest -v tests/scripts/test_return_calculations.py

import unittest
import pandas as pd
import move_two_levels_up
from scripts import return_calculations as rt

# Tests
#################
#  1. merge_df()
#  2. subtract_column()
#  3. test_df_column_to_int():
#  4. test_add_ratio_column():
#  5. test_drop_column():


class TestReturnCalculations(unittest.TestCase):
    # Test class that inherits from  unittest.testacse
    # Gives access to testing capabilities.

    def test_merge_df(self):
        # Setup
        df1 = pd.DataFrame({
                'col_a': ['a1', 'a2', 'a3'],
                'col_b': ['b1', 'b2', 'b3'],
            })
        df2 = pd.DataFrame({
                'col_c': ['c1', 'c2', 'c3'],
                'col_d': ['d1', 'd2', 'd3'],
            })
        # Call function
        actual = rt.merge_df(df1, df2)
        # Expectation
        expected = pd.DataFrame({
                'col_a': ['a1', 'a2', 'a3'],
                'col_b': ['b1', 'b2', 'b3'],
                'col_c': ['c1', 'c2', 'c3'],
                'col_d': ['d1', 'd2', 'd3'],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_subtract_column(self):
        # Setup
        df1 = pd.DataFrame({
                'col_a': [50, 50, 50],
                'col_b': [30, 30, 30],
            })
        # Call function
        actual = rt.subtract_column(df1, 'col_a', 'col_b', 'col_c')
        # Expectation
        expected = pd.DataFrame({
                'col_a': [50, 50, 50],
                'col_b': [30, 30, 30],
                'col_c': [20, 20, 20],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_df_column_to_int(self):
        # Setup
        df1 = pd.DataFrame({
            'col_a': [50.7, 50.8, 50.9],
            'col_b': [30.3, 30.4, 30.5],
            })
        # Call function
        actual = rt.df_column_to_int(df1, 'col_a')
        # Expectation
        expected = pd.DataFrame({
            'col_a': [50, 50, 50],
            'col_b': [30.3, 30.4, 30.5],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_add_ratio_column(self):
        # Setup
        df1 = pd.DataFrame({
                'col_a': [100, 200, 400],
                'col_b': [200, 400, 800],
            })
        # Call function
        actual = rt.add_ratio_column(
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
