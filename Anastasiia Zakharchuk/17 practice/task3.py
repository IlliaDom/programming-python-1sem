import sys
import requests

URL = "https://api.open-meteo.com/v1/forecast"

CITY = "Lutsk"
LATITUDE = 50.7534
LONGITUDE = 25.3308

params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "current": "temperature_2m,wind_speed_10m",
}

try:
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Помилка запиту: {e}", file=sys.stderr)
    sys.exit(1)

data = response.json()
current = data["current"]
units = data["current_units"]

temp = current["temperature_2m"]
wind = current["wind_speed_10m"]

print("Анастасія Захарчук, ІТ-32")
print(
    f'{CITY} ({LATITUDE}, {LONGITUDE}): '
    f'{temp} {units["temperature_2m"]}, '
    f'wind {wind} {units["wind_speed_10m"]}'
)