
# imports
import requests
import json
import pandas as pd
import time


# pulling data from balldontlie.io API
# wrote down number of pages for ease of program
player_pages = 151


# loop to pull all player data
for x in range(1, player_pages+1):
    player_url = f'https://www.balldontlie.io/api/v1/players?page={x}'
    r = requests.get(player_url)
    j = r.json()['data']
    df = pd.DataFrame.from_dict(j)
    df.to_csv(f'RawText/players{x}.csv', index=False)
    time.sleep(5)