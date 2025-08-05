import sqlite3
from datetime import datetime

DB_FILE = "jackpots.db"

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

def save_jackpots(jackpots):
    timestamp = datetime.now().isoformat()
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.executemany('''
            INSERT INTO jackpots (timestamp, game, jackpot)
            VALUES (?, ?, ?)
        ''', [(timestamp, game, amount) for game, amount in jackpots.items()])
        conn.commit()
