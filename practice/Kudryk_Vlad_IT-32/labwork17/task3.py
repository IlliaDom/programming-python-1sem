import sys
import requests

print("Vlad Kudryk, IT-32")

URL = "https://api.open-meteo.com/v1/forecast"
CITY = "Kyiv"
LAT = 50.45
LON = 30.52

params = {
    "latitude": LAT,
    "longitude": LON,
    "current": "temperature_2m,wind_speed_10m",
}

try:
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.RequestException as e:
    print("Request error:", e, file=sys.stderr)
    sys.exit(1)

current = data["current"]
units = data["current_units"]
temp = current["temperature_2m"]
wind = current["wind_speed_10m"]
print(f"{CITY} ({LAT}, {LON}): {temp} {units['temperature_2m']}, wind {wind} {units['wind_speed_10m']}")