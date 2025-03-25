import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        city TEXT,
        temp REAL,
        feels_like REAL,
        humidity REAL,
        wind_speed REAL,
        pressure REAL,
        visibility REAL,
        condition TEXT,
        timestamp TEXT
    )
''')

conn.commit()
conn.close()

print(" 'weather' table created successfully.")
