# Script to set a connection to MySQL to save data

from sqlalchemy import create_engine

# Connect to MySQL database
##############################################################################
url = 'mysql+pymysql://root:password1@localhost:3306/PCL_database'
engine = create_engine(url)
