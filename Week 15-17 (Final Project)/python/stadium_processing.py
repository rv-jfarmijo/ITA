
# import libraries
import sqlite3
import pandas as pd
import os
import ast


# setup sqlite connection
con = sqlite3.connect('../airflow/airflow.db')
cur = con.cursor()


# import stadium data from csv
raw_stadiums=pd.read_csv('../RawText/stadiums.csv')


# Keep only the columns in sql table
stadiums = raw_stadiums[['Arena', 'City', 'State', 'Capacity', 'Opened']]



# write to sql database
stadiums.to_sql(name = 'arena', con=con, index=False, if_exists='append')


# finalize and close connections
con.commit()
cur.close()
con.close()



