import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT * FROM weather
    WHERE timestamp LIKE '2016-03-23%'
    LIMIT 5
""")

rows = cursor.fetchall()
if rows:
    for row in rows:
        print(row)
else:
    print(" No data found for 2016-03-23.")

conn.close()
