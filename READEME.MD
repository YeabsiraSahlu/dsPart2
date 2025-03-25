# ETL Weather Data Project

Created by: Miky Asmare, Soliyana Yohannes, Nathan Ressom, Yeabsira Sahlu, and Dan Bezabhe

## Overview

This project demonstrates the development of an ETL (Extract, Transform, Load) pipeline using real-world weather data. It was completed as part of the DS2002 Data Project 1 and meets the objectives of data ingestion, transformation, storage, and analysis using both API and flat file sources.

## Project Structure

- **Source 1 (API):** Real-time weather data is pulled from OpenWeatherMap using an API key securely stored in a `.env` file.
- **Source 2 (CSV):** Historical weather data for Washington, DC from 2015–2024 was retrieved from Kaggle and loaded from a local CSV file.
- **Transformation:** The raw CSV data is cleaned and mapped to match the structure of the API response. Data is transformed and formatted to be inserted into a SQLite database.
- **Loading:** Both sources are stored in a `weather` table inside `database.db` using SQLite.
- **Comparison:** We compare the current weather data from the API to historical data on the same date (e.g., March 23, 2016) from the CSV source to analyze temperature, humidity, and wind speed trends over time.
- **Summary & Debugging Tools:** Custom scripts list city names, check years available in the database, and inspect specific entries.

## Files

- `weather.py` – Fetches current weather data from OpenWeatherMap API.
- `load_csv.py` – Loads the historical weather CSV into the database.
- `save_to_db.py` – Contains a helper function for inserting API data.
- `compare_weather.py` – Compares current weather to historical data from the same day.
- `init_db.py` – Initializes the SQLite database and creates the `weather` table.
- `view_data.py` – Displays available years from the database.
- `list_cities.py` – Lists distinct cities saved in the database.
- `.env` – Stores the API key (excluded from version control using `.gitignore`).
- `database.db` – SQLite database storing all ingested weather records.

## Features

- Ingests data from both remote and local sources.
- Dynamically creates and populates a SQL database.
- Compares and analyzes trends between current and past weather conditions.
- Implements structured error handling during ingestion and insertion.
- Clean project structure for easy collaboration via Git and GitHub.

## Getting Started

1. Clone the repo.
2. Create a virtual environment and install dependencies:

```bash
pip install -r requirements.txt
