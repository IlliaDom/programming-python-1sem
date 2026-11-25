import sys

import requests

NAME = "Назар, лабораторна 38"  # заміни на своє ім'я та групу
URL = "https://api.open-meteo.com/v1/forecast"

CITY = "Kyiv"
LATITUDE = 50.4501
LONGITUDE = 30.5234


def main() -> int:
    print(NAME)

    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current": "temperature_2m,wind_speed_10m",
    }

    try:
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"Помилка запиту: {exc}", file=sys.stderr)
        return 1

    data = response.json()
    current = data["current"]
    units = data["current_units"]

    temp = current["temperature_2m"]
    temp_unit = units["temperature_2m"]
    wind = current["wind_speed_10m"]
    wind_unit = units["wind_speed_10m"]

    print(
        f"{CITY} ({LATITUDE}, {LONGITUDE}): "
        f"{temp} {temp_unit}, wind {wind} {wind_unit}"
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
