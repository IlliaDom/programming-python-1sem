import requests
import sys

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 50.7472,
    "longitude": 25.3254,
    "current": "temperature_2m,wind_speed_10m"
}

try:
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

except requests.RequestException as error:
    print(f"Network error: {error}", file=sys.stderr)
    sys.exit(1)

current = data["current"]
units = data["current_units"]

print("Vlad Mushka, IT31")
print(f'Lutsk (50.7472, 25.3254):')
print(f'Temperature: {current["temperature_2m"]} {units["temperature_2m"]}')
print(f'Wind: {current["wind_speed_10m"]} {units["wind_speed_10m"]}')
