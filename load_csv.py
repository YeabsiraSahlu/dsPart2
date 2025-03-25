import sqlite3
import pandas as pd
from datetime import datetime

csv_file = "dc_weather.csv"
df = pd.read_csv(csv_file)

print(" Columns in CSV:", df.columns.tolist())

df["timestamp"] = pd.to_datetime(df["datetime"], errors='coerce').dt.strftime('%Y-%m-%d')

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        city TEXT,
        temp REAL,
        feels_like REAL,
        humidity INTEGER,
        wind_speed REAL,
        pressure REAL,
        visibility REAL,
        condition TEXT,
        timestamp TEXT
    )
''')

for index, row in df.iterrows():
    try:
        cursor.execute('''
            INSERT INTO weather (city, temp, feels_like, humidity, wind_speed, pressure, visibility, condition, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            row.get("name", None),
            row.get("temp", None),
            row.get("feelslike", None),
            row.get("humidity", None),
            row.get("windspeed", None),
            row.get("sealevelpressure", None),
            row.get("visibility", None),
            row.get("conditions", None),
            row.get("timestamp", None)
        ))
    except Exception as e:
        print(f" Error at row {index}: {e}")
        continue

conn.commit()
conn.close()
print(" CSV data successfully loaded into database.")
