import sqlite3 as db

with db.connect('bank.db') as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner TEXT NOT NULL,
        balance INTEGER NOT NULL DEFAULT 0
        )""")