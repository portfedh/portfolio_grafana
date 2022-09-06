# Run using:
# $ python3 -m unittest -v tests/scripts/test_irr_calculations.py

import unittest
import pandas as pd
from pandas import Timestamp
import move_two_levels_up
from scripts import irr_calculations as irr


class TestReturnCalculations(unittest.TestCase):
    # Test class that inherits from  unittest.testacse
    # Gives access to testing capabilities.

    def test_concat_df(self):
        # Setup
        df1 = pd.DataFrame({
            'col_a': [1, 2],
            'col_b': [3, 4],
            })
        df2 = pd.DataFrame({
            'col_a': [5, 6],
            'col_b': [7, 8],
            })
        # Call function
        actual = irr.concat_df(df1, df2)
        actual = actual.reset_index(drop=True)
        # Expectation
        expected = pd.DataFrame({
            'col_a': [1, 2, 5, 6],
            'col_b': [3, 4, 7, 8],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_to_datetime_df(self):
        # Setup
        df1 = pd.DataFrame({
                'Date': ['29/01/21', '30/01/21', '31/01/21'],
                'Values': [99, 100, 101],
            })
        # Call function
        actual = irr.to_datetime_df(df1, 'Date')
        # Expectation
        data = {'Values': [99, 100, 101]}
        index = pd.date_range('29/01/21', periods=3)
        expected = pd.DataFrame(data, index=index)
        expected = expected.rename_axis('Date', axis=1)
        # Test
        pd.testing.assert_frame_equal(actual, expected, check_freq=False)

    def test_add_total_df(self):
        # Setup
        df1 = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [4, 5, 6],
            })

        # Call function
        actual = irr.add_total_df(df1, 'col_c')

        # Expectation
        expected = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [4, 5, 6],
            'col_c': [5, 7, 9],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_filter_df(self):
        # Setup
        df1 = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [4, 5, 6],
            'col_c': [7, 8, 9],
            'col_d': [10, 11, 12],
            })
        # Call function
        actual = irr.filter_df(df1, ['col_a', 'col_c'])
        # Expectation
        expected = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_c': [7, 8, 9],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_invert_cf_df(self):
        # Setup
        df1 = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [4, 5, 6],
            })
        # Call function
        actual = irr.invert_cf_df(df1, 'col_b')
        # Expectation
        expected = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [-4, -5, -6],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_integers_df(self):
        # Setup
        df1 = pd.DataFrame({
            'col_a': [1.4, 2.5, 3.6],
            'col_b': [4.7, 5.8, 6.9],
            })
        # Call function
        actual = irr.integers_df(df1, 'col_b')

        # Expectation
        expected = pd.DataFrame({
            'col_a': [1.4, 2.5, 3.6],
            'col_b': [4, 5, 6],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_merge_df(self):
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
        actual = irr.merge_df(df1, df2)
        # Expectation
        expected = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [4, 5, 6],
            'col_c': [7, 8, 9],
            'col_d': [10, 11, 12],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_get_last_value(self):
        # Setup
        df1 = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [4, 5, 6],
            })
        # Call function
        actual = irr.get_last_value(df1)
        actual = actual.reset_index(drop=True)
        # Expectation
        expected = pd.DataFrame({
            'col_a': [3],
            'col_b': [6],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_rename_column(self):
        # Setup
        df1 = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_b': [4, 5, 6],
            })
        # Call function
        actual = irr.rename_column(df1, 'col_b', 'col_new')
        # Expectation
        expected = pd.DataFrame({
            'col_a': [1, 2, 3],
            'col_new': [4, 5, 6],
            })
        # Test
        pd.testing.assert_frame_equal(actual, expected)

    def test_split_df(self):
        # Setup
        data = {'Values': [99, 100, 101]}
        index = pd.date_range('29/01/21', periods=3)
        df1 = pd.DataFrame(data, index=index)
        df1 = df1.rename_axis('Date', axis=1)
        # Call function
        dates_actual, values_actual = irr.split_df(df1, 'Values')
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
