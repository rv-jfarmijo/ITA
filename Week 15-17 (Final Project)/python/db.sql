--- sudo -u postgres psql

create table players(
    PlayerID int PRIMARY KEY UNIQUE NOT NULL,
    FirstName varchar(30) NOT NULL, 
    LastName varchar(50) NOT NULL, 
    Position varchar(10),
    TeamID int NOT NULL
    );


create table teams(
    TeamID int PRIMARY KEY UNIQUE NOT NULL,
    Abbreviation varchar (10),
    City varchar (50),
    Conference varchar(10),
    Division varchar(25),
    FullName varchar(75),
    TeamName varchar(25)
);

create table arena(
    Arena varchar(75) PRIMARY KEY UNIQUE NOT NULL,
    City varchar(25),
    State varchar(25),
    Capacity int,
    Opened int
);

PRAGMA table_info(table_name);

select ID, date, hometeamid, home_team_score, postseason, season, status, time, awayteamid, visitor_team_score from games1 limit 10;

create temporary table games_v1 as
select a.date_clean as date, b.TeamID as AwayTeamID, a.PTS as AwayTeamPoints, a.[Home/Neutral], a.[PTS.1] as HomeTeamPoints, a.[Attend.] as Attendance
from games2 a
join teams b
on a.[Visitor/Neutral] = b.FullName;

create temporary table games_v2 as
select a.date, b.TeamID as HomeTeamID, a.HomeTeamPoints, a.AwayTeamID, a.AwayTeamPoints, a.Attendance
from games_v1 a
join teams b
on a.[Home/Neutral] = b.FullName;

create  table games as
select b.id as GameID, a.*, d.Arena
from games_v2 a
join games1 b
on a.date = b.date_clean
and a.HomeTeamID = b.HomeTeamID
and a.AwayTeamID = b.AwayTeamID
join teams c
on a.HomeTeamID = c.TeamID
join arena d
on c.City = d.City
where b.postseason = 0;


--Query for loading games through airflow

insert into games(date, HomeTeamID, HomeTeamPoints, AwayTeamID, AwayTeamPoints, Attendance, arena)
select a.date, coalesce(b.TeamID, f.TeamID) as HomeTeamID, 
    a.homescore as HomeTeamPoints, coalesce(c.TeamID, i.TeamID) as AwayTeamID, 
    a.awayscore as AwayTeamPoints, a.attendance as Attendance, 
    'jjj' as Arena
    --coalesce(d.Arena, g.Arena, j.Arena) as Arena
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



create table City_Team_join(
    gin varchar(50),
    gout varchar(50)
);

insert into City_Team_join(gin, gout)
values('LA Lakers', 'Lakers'),
('Golden State', 'Warriors'),
('Indiana', 'Pacers'),
('Minnesota', 'Timberwolves'),
('Utah', 'Jazz'),
('New York', 'Knicks');

select count(*) from cases a
join arena b
on a.City = b.City
join games c
on a.date = c.date
and b.arena = c.arena 
where a.cases is not null;