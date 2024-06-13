import sqlite3

conn = sqlite3.connect('db/expense_tracker.db')
cursor = conn.cursor()

#table category
cursor.execute("""
    CREATE TABLE IF NOT EXISTS category(
    id INTEGER PRIMARY KEY,
    name TEXT
    )
""")
conn.commit()

#table expense
cursor.execute ("""
    CREATE TABLE IF NOT EXISTS expense(
    id INTEGER PRIMARY KEY,
    description TEXT,
    amount REAL,
    date TEXT,
    category_id INTEGER,
    user_id INTEGER
    )
    """
)
conn.commit()

#table user
cursor.execute ("""
    CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY,
    name TEXT,
    password TEXT
    )
    """
)
conn.commit()
