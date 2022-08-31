# Run using:
# $ python3 -m unittest -v tests/scripts/test_irr_calculations.py

import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal
import move_two_levels_up
from scripts import irr_calculations as irr

# Tests
#######
# 1. concat_df()        [Pendiente]
# 2. to_datetime_df()   [Done]
# 3. add_total_df()
# 4. filter_df()
# 5. invert_cf_df()
# 6. integers_df()
# 7. merge_df()
# 8. get_last_value()
# 9. rename_column()
# 10. split_df()


class TestReturnCalculations(unittest.TestCase):
    # Test class that inherits from  unittest.testacse
    # Gives access to testing capabilities.

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
        assert_frame_equal(actual, expected, check_freq=False)


if __name__ == "__main__":
    unittest.main()
