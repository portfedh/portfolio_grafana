import pandas as pd
import datetime as dt

# Set analysis dates
start_date = "2018-01-01"
end_date = dt.date.today()
date_range = pd.date_range(start=start_date, end=end_date)
