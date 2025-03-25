import sqlite3

def save_to_db(city, temp, feels_like, humidity, wind_speed, pressure, visibility, condition):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temp REAL,
            feels_like REAL,
            humidity INTEGER,
            wind_speed REAL,
            pressure INTEGER,
            visibility REAL,
            condition TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        INSERT INTO weather (city, temp, feels_like, humidity, wind_speed, pressure, visibility, condition)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (city, temp, feels_like, humidity, wind_speed, pressure, visibility, condition))

    conn.commit()
    conn.close()
    print(" Weather data saved to database.")
