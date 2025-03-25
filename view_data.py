import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT DISTINCT strftime('%Y', timestamp) FROM weather")
rows = cursor.fetchall()

print("Years in database:")
for row in rows:
    print(f"- {row[0]}")

conn.close()
