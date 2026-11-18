import requests
import sys

print("Nikita Krilovets, IT-31")

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
    units = data["current_units"]

    print(
        f"Lutsk (50.75, 25.34): "
        f"{current['temperature_2m']} {units['temperature_2m']}, "
        f"wind {current['wind_speed_10m']} {units['wind_speed_10m']}"
    )

except requests.RequestException as error:
    print(error, file=sys.stderr)
    sys.exit(1)
