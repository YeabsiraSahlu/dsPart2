import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT DISTINCT city FROM weather")
cities = cursor.fetchall()

print("Cities in the database:")
for city in cities:
    print("-", city[0])

conn.close()
