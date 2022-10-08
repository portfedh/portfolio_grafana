# Script to set dates for the portfolio analysis

import pandas as pd
import datetime as dt

# Set analysis dates
start_date = "2019-01-15"
end_date = dt.date.today()
date_range = pd.date_range(start=start_date, end=end_date)
