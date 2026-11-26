import sys
import requests

NAME = "Nazar Mischuk, IT-32"  

CITY = "Kyiv"
LATITUDE = 50.45
LONGITUDE = 30.52

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "current": "temperature_2m,wind_speed_10m",
}

try:
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.RequestException as error:
    print("Помилка запиту:", error, file=sys.stderr)
    sys.exit(1)

temperature = data["current"]["temperature_2m"]
wind = data["current"]["wind_speed_10m"]
temp_unit = data["current_units"]["temperature_2m"]
wind_unit = data["current_units"]["wind_speed_10m"]

print(NAME)
print(f"{CITY} ({LATITUDE}, {LONGITUDE}): {temperature} {temp_unit}, wind {wind} {wind_unit}")
