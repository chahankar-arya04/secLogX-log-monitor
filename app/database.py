import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    # Create table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Insert a test user (username: admin, password: admin123)
    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "admin123"))
    conn.commit()
    conn.close()
