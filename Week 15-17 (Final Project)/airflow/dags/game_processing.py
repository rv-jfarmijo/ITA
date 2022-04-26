## export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH must run every time 
## before webserver and scheduler

from socket import if_indextoname
from unicodedata import name
from airflow.models import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup

from datetime import datetime
import requests
from bs4 import BeautifulSoup
import time
import sqlite3
import pandas as pd



default_args = {
    'start_date': datetime(2022, 3, 24), 
    'email': ['jarred.armijo@gmail.com'],
    'email_on_failure': True,
    'retries': 1,
}
def get_game_scores(ti):
#scrape new game data
    url = 'https://www.basketball-reference.com/boxscores/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    game_sums = soup.find_all('div', {'class': 'game_summary expanded nohover'})
    game_sums_list = []
    for x in range(0, len(game_sums)):
        game_sum = game_sums[x].table
        counter = 0
        game_summary = {}
        ah_indicator = ['away', 'home']
        for tr in game_sum.find_all('tr'):
            game_deets = {
                f'{ah_indicator[counter]}team': tr.find('a').get_text(),
                f'{ah_indicator[counter]}score': tr.find('td', {'class': 'right'}).get_text()
            }
            counter +=1
            game_summary.update(game_deets)
        game_summary['game_url'] = 'https://www.basketball-reference.com' + game_sum.find(
            'td',
            {'class': 'right gamelink'}).find('a', href=True)['href']
        game_sums_list.append(game_summary)
    ti.xcom_push(key='get_game', value = game_sums_list)

def get_game(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    game_title = soup.find('h1').get_text()
    game_date = datetime.strftime(
        datetime.strptime(game_title.split('Score, ')[1], "%B %d, %Y"),
        '%Y-%m-%d'
    )
    scoreboard = soup.find(
        'div', {'class': 'scorebox'}).find(
        'div', {'class': 'scorebox_meta'}).find_all('div')
    arena = scoreboard[1].get_text()
    text = 'Attendance'
    try:
        attendance = ''.join(filter(str.isdigit, soup.find(
            lambda tag: tag.name =='strong' and text in tag.text).find_parent().get_text()))
    except AttributeError:
        attendance = None
    return {'date': game_date, 'arena': arena, 'attendance': attendance}  

def game_complete(ti):
    games = ti.xcom_pull(key='get_game', task_ids=['get_game_sums'])
    # print(games[0][0]['game_url'])
    for x in games[0]:
        # print(x['awayteam'])
        game_details = get_game(x['game_url'])
        x.update(game_details)
        time.sleep(3)
    ti.xcom_push(key='get_game_complete', value = games)

def load_games(ti):
    con = sqlite3.connect('//home/ec2-user/airflow/airflow.db')
    cur = con.cursor()
    load_file = ti.xcom_pull(key='get_game_complete', task_ids=['get_game_complete'])[0][0]
    new_games = pd.DataFrame(load_file)
    new_games_load = new_games[['date', 'hometeam', 'homescore', 'awayteam', 'awayscore', 'attendance', 'arena']]
    # cur.execute('select * from games limit 1;')
    # print(cur.fetchall())
    new_games_load.to_sql(name= 'games_load', con=con, index=False, if_exists='replace')
    # finalize and close connections
    con.commit()
    cur.close()
    con.close()

with DAG('game_processing', schedule_interval='@daily', 
        default_args=default_args, 
        catchup = False) as dag:

    get_game_sums = PythonOperator(
        task_id = 'get_game_sums',
        python_callable = get_game_scores
    )

    get_game_complete = PythonOperator(
        task_id = 'get_game_complete',
        python_callable=game_complete
    )

    load_games_sql = PythonOperator(
        task_id = 'load_games_sql',
        python_callable=load_games
    )

    process_games_sql = SqliteOperator(
        task_id = 'process_games_sql',
        sqlite_conn_id = 'db_sqlite',
        sql = """
        insert into games(date, HomeTeamID, HomeTeamPoints, AwayTeamID, AwayTeamPoints, Attendance, arena)
        select a.date, coalesce(b.TeamID, f.TeamID) as HomeTeamID, 
            a.homescore as HomeTeamPoints, coalesce(c.TeamID, i.TeamID) as AwayTeamID, 
            a.awayscore as AwayTeamPoints, a.attendance as Attendance, 
            coalesce(d.Arena, g.Arena, j.Arena) as Arena
        from games_load a
        left join teams b
        on a.hometeam = b.City
        left join teams c
        on a.awayteam = c.City
        left join arena d
        on b.City = d.City
        left join City_Team_join e
        on a.hometeam = e.gin
        left join teams f
        on e.gout = f.TeamName
        left join arena g
        on f.City = g.City
        left join City_Team_join h
        on a.awayteam = h.gin
        left join teams i
        on h.gout = i.TeamName
        left join arena j
        on i.City = j.City;
        """

    )

    get_game_sums >> get_game_complete >> load_games_sql >> process_games_sql