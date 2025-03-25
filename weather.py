import requests
import os
from save_to_db import save_to_db

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Washington, D.C"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()

    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    pressure = data["main"]["pressure"]
    visibility = data.get("visibility", 10000) / 1000
    weather_desc = data["weather"][0]["description"].capitalize()

    print("\n  Weather Report  ")
    print("=" * 40)
    print(f" Location: {CITY}")
    print(f" Temperature: {temp:.1f}°C (Feels like {feels_like:.1f}°C)")
    print(f" Condition: {weather_desc}")
    print(f" Humidity: {humidity}%")
    print(f" Wind Speed: {wind_speed} m/s")
    print(f" Visibility: {visibility:.2f} km")
    print(f" Pressure: {pressure} hPa")
    print("=" * 40)

    save_to_db(CITY, temp, feels_like, humidity, wind_speed, pressure, visibility, weather_desc)
else:
    print(f" Error {response.status_code}: {response.text}")
