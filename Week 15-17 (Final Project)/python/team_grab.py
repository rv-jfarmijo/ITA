
# imports
import requests
import pandas as pd



# pulling data from balldontlie.io API

# all teams on one page
team_url = 'https://www.balldontlie.io/api/v1/teams'


# pull team data    
r = requests.get('https://www.balldontlie.io/api/v1/teams')
j = r.json()['data']
df = pd.DataFrame.from_dict(j)
df.to_csv('RawText/teams.csv', index=False)