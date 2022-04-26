# requests
import requests
import pandas as pd
import time



# pulling data from balldontlie.io API


# Game data pull
game_pages = 100


for page in range(1, game_pages+1):
    games_url = f'https://www.balldontlie.io/api/v1/games?start_date=2020-12-20&page={page}'
    r = requests.get(games_url)
    j = r.json()['data']
    df = pd.DataFrame.from_dict(j)
    df.to_csv(f'../RawText/games{page}.csv', index=False)
    time.sleep(5)
