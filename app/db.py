import sqlite3
from datetime import datetime

# using data/ so that the volume is persisted in Docker and isn't destroyed anytime the container is rebuilt
DB_FILE = "data/jackpots.db"

def create_table():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jackpots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                game TEXT NOT NULL,
                jackpot TEXT NOT NULL
            )
        ''')
        conn.commit()

# this when run will grab the game and amount values and insert them into the SQLite table long with the timestamp when run
def save_jackpots(jackpots):
    timestamp = datetime.now().isoformat()
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.executemany('''
            INSERT INTO jackpots (timestamp, game, jackpot)
            VALUES (?, ?, ?)
        ''', [(timestamp, game, amount) for game, amount in jackpots.items()])
        conn.commit()
