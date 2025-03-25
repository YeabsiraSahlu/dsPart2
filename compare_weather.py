import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

API_CITY = "Washington, D.C"
CSV_CITY = "Washington,DC,USA"

cursor.execute('''
    SELECT city, temp, feels_like, humidity, wind_speed, pressure, visibility, condition, timestamp
    FROM weather
    WHERE city = ?
    ORDER BY timestamp DESC
    LIMIT 1
''', (API_CITY,))
latest = cursor.fetchone()

cursor.execute('''
    SELECT city, temp, feels_like, humidity, wind_speed, pressure, visibility, condition, timestamp
    FROM weather
    WHERE city = ?
    AND timestamp LIKE '2016-03-23%'
    ORDER BY timestamp ASC
    LIMIT 1
''', (CSV_CITY,))
oldest = cursor.fetchone()

conn.close()

if not latest:
    print("No current weather data (from API) found.")
if not oldest:
    print("No historical weather data (from CSV) found.")
if not latest or not oldest:
    print("Could not find both current and historical weather data.")
else:
    (city1, temp1, feels1, humid1, wind1, press1, visib1, cond1, time1) = latest
    (city2, temp2, feels2, humid2, wind2, press2, visib2, cond2, time2) = oldest

    print("\nCurrent Weather (from API):")
    print(f"City: {city1}, Temp: {temp1}°C, Feels Like: {feels1}°C, Humidity: {humid1}%, Wind: {wind1} m/s, Time: {time1}")

    print("\nHistorical Weather (from CSV - 2016-03-23):")
    print(f"City: {city2}, Temp: {temp2}°C, Feels Like: {feels2}°C, Humidity: {humid2}%, Wind: {wind2} m/s, Time: {time2}")

    print("\nComparison:")
    print(f"Temperature difference: {temp1 - temp2:.2f}°C")
    print(f"Humidity difference: {humid1 - humid2}%")
    print(f"Wind speed difference: {wind1 - wind2:.2f} m/s")
