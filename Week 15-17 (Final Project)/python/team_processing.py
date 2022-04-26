

# import libraries
import sqlite3
import pandas as pd
import os
import ast



# setup sqlite connection
con = sqlite3.connect('../airflow/airflow.db')
cur = con.cursor()



# import team data from csv
raw_teams=pd.read_csv('../RawText/teams.csv')



# rename columns to match sql table
raw_teams.rename(columns = {
    'id': 'TeamID', 'abbreviation': 'Abbreviation',
    'city': 'City', 'conference': 'Conference', 'division': 'Division',
    'full_name': 'FullName', 'name': 'TeamName'
}, inplace = True)



# write to sql database
raw_teams.to_sql(name = 'teams', con=con, index=False, if_exists='append')



# finalize and close connections
con.commit()
cur.close()
con.close()



