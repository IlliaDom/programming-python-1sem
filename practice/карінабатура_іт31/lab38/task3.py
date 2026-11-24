# task3.py
import sys
import requests

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
except requests.RequestException as e:
    print(f"Помилка отримання погоди: {e}", file=sys.stderr)
    sys.exit(1)

current = data.get("current", {})
temp = current.get("temperature_2m")
wind_speed = current.get("wind_speed_10m")
temp_unit = data.get("current_units", {}).get("temperature_2m", "°C")
wind_unit = data.get("current_units", {}).get("wind_speed_10m", "km/h")

print("Батура Каріна Віталіївна, ІТ-31")
print(f"Lutsk (50.75, 25.34): {temp} {temp_unit}, wind {wind_speed} {wind_unit}")