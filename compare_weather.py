import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

CITY = "Washington"

cursor.execute('''
    SELECT city, temp, feels_like, humidity, wind_speed, pressure, visibility, condition, timestamp
    FROM weather
    WHERE city LIKE ?
    ORDER BY timestamp DESC
    LIMIT 1
''', (f"%{CITY}%",))
latest = cursor.fetchone()

cursor.execute('''
    SELECT city, temp, feels_like, humidity, wind_speed, pressure, visibility, condition, timestamp
    FROM weather
    WHERE city LIKE ?
    ORDER BY timestamp ASC
    LIMIT 1
''', (f"%{CITY}%",))
oldest = cursor.fetchone()

conn.close()

if not latest or not oldest:
    print(" Could not find both current and historical weather data.")
else:
    (city1, temp1, feels1, humid1, wind1, press1, visib1, cond1, time1) = latest
    (city2, temp2, feels2, humid2, wind2, press2, visib2, cond2, time2) = oldest

    print("\n Current Weather (API):")
    print(f"City: {city1}, Temp: {temp1}°C, Feels Like: {feels1}°C, Humidity: {humid1}%, Wind: {wind1} m/s, Time: {time1}")

    print("\n Historical Weather (CSV):")
    print(f"City: {city2}, Temp: {temp2}°C, Feels Like: {feels2}°C, Humidity: {humid2}%, Wind: {wind2} m/s, Time: {time2}")

    print("\n Comparison:")
    print(f" Temperature difference: {temp1 - temp2:.2f}°C")
    print(f" Humidity difference: {humid1 - humid2}%")
    print(f" Wind speed difference: {wind1 - wind2:.2f} m/s")
