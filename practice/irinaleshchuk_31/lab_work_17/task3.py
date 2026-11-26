
import requests
import sys

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 50.75,
    "longitude": 25.34,
    "current": "temperature_2m,wind_speed_10m"
}

try:
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    current = data["current"]

    print("Лещук Ірина, IT-31")
    print("Lutsk (50.75, 25.34):")
    print(f"Temperature: {current['temperature_2m']} °C")
    print(f"Wind: {current['wind_speed_10m']} km/h")

except requests.RequestException as error:
    print(f"Помилка запиту: {error}", file=sys.stderr)
    sys.exit(1)
