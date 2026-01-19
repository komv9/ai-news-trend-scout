# agent/memory.py
import sqlite3

DB_PATH = "data/trends.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS insights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            summary TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_insight(date, summary):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO insights (date, summary) VALUES (?, ?)",
        (date, summary)
    )
    conn.commit()
    conn.close()
