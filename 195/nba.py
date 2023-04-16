from collections import namedtuple
import csv
import os
from pathlib import Path
import sqlite3
import random
import string

import requests

DATA_URL = "https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm"
TMP = Path(os.getenv("TMP", "/tmp"))

salt = "".join(random.choice(string.ascii_lowercase) for i in range(20))
DB = TMP / f"nba_{salt}.db"

Player = namedtuple(
    "Player", ("name year first_year team college active " "games avg_min avg_points")
)

conn = sqlite3.connect(DB)
cur = conn.cursor()


def import_data():
    with requests.Session() as session:
        content = session.get(DATA_URL).content.decode("utf-8")

    reader = csv.DictReader(content.splitlines(), delimiter=",")

    players = []
    for row in reader:
        players.append(
            Player(
                name=row["Player"],
                year=row["Draft_Yr"],
                first_year=row["first_year"],
                team=row["Team"],
                college=row["College"],
                active=row["Yrs"],
                games=row["Games"],
                avg_min=row["Minutes.per.Game"],
                avg_points=row["Points.per.Game"],
            )
        )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS players
                  (name, year, first_year, team, college, active,
                  games, avg_min, avg_points)"""
    )
    cur.executemany("INSERT INTO players VALUES (?,?,?,?,?,?,?,?,?)", players)
    conn.commit()


import_data()


# you code:


def player_with_max_points_per_game():
    """The player with highest average points per game (don't forget to CAST to
    numeric in your SQL query)"""
    stmt = (
        "select name, cast(avg_points as real) "
        "from players "
        "group by name "
        "order by cast(avg_points as real) desc "
        "limit 1"
    )
    cur.execute(stmt)
    player, _ = cur.fetchone()
    return player


def number_of_players_from_duke():
    """Return the number of players with college == Duke University"""
    stmt = "select count(1) from players where college = 'Duke University'"
    cur.execute(stmt)
    no_players = int(cur.fetchone()[0])
    return no_players


def avg_years_active_players_stanford():
    """Return the average years that players from "Stanford University
    are active ("active" column)"""
    stmt = (
        "select name, cast(active as real) "
        "from players "
        "where college = 'Stanford University' "
    )
    cur.execute(stmt)

    rows = cur.fetchall()
    total = sum(item[1] for item in rows)

    return round(total / len(rows), 2)


def year_with_most_new_players():
    """Return the year with the most new players.
    Hint: you can use GROUP BY on the year column.
    """
    # stmt = "select * from players where first_year <> '0'"

    stmt = (
        "select year, count(first_year) "
        "from players "
        "where first_year = '0'"
        "group by year "
        "order by count(first_year) desc "
        "limit 1"
    )
    cur.execute(stmt)
    year, _ = cur.fetchone()
    return year
