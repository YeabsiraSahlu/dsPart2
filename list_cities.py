import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT DISTINCT city FROM weather")
cities = cursor.fetchall()

print(" Unique city names in database:")
for city in cities:
    print(f"- {city[0]}")

conn.close()
