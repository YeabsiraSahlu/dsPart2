import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute('''
    SELECT city, temp, timestamp
    FROM weather
    ORDER BY timestamp ASC
    LIMIT 10
''')

rows = cursor.fetchall()
print("\n Oldest entries in weather table:")
print("=" * 40)
for row in rows:
    city, temp, timestamp = row
    print(f"City: {city}, Temp: {temp}°C, Timestamp: {timestamp}")

conn.close()
