
# import libraries
import sqlite3
import pandas as pd
import os
import ast


# setup sqlite connection
con = sqlite3.connect('../airflow/airflow.db')
cur = con.cursor()


# prepare player files and load into df
file_list = os.listdir('../RawText')
player_files = [x for x in file_list if x.startswith('players')]
li = []
for file in player_files:
    df=pd.read_csv(f'../RawText/{file}')
    li.append(df)
players_raw = pd.concat(li)



# extract teamid from team dictionary
players_raw['teamid'] = players_raw.apply(lambda row: ast.literal_eval(row['team'])['id'], axis=1)



# grab only columns going to database
players_clean = players_raw[['id', 'first_name', 'last_name', 'position', 'teamid']]



# rename columns so they match sql table
players_clean.rename(columns = {'id': 'PlayerID', 'first_name': 'FirstName', 'last_name': 'LastName', 'position': 'Position', 'teamid': 'TeamID'}, inplace = True)



# Clean up some bad data
players_clean['LastName'] = players_clean['LastName'].fillna(value='None')
players_clean.drop_duplicates(inplace=True)



# write to sql database
players_clean.to_sql(name = 'players', con=con, index=False, if_exists='append')



# finalize and close connections
con.commit()
cur.close()
con.close()

