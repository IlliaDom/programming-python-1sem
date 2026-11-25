import sys

import requests

NAME, SURNAME, GROUP = "Sofiia", "Zakharchuk", "IT-32"

CITY = "Lutsk"
LATITUDE, LONGITUDE = 50.75, 25.34

URL = "https://api.open-meteo.com/v1/forecast"


def main() -> None:
    print(f"{NAME} {SURNAME}, {GROUP}")
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current": "temperature_2m,wind_speed_10m",
    }
    try:
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        current, units = data["current"], data["current_units"]
    except requests.RequestException as error:
        print(f"error: {error}", file=sys.stderr)
        sys.exit(1)
    except KeyError as error:
        print(f"error: unexpected answer, no field {error}", file=sys.stderr)
        sys.exit(1)

    temp = f"{current['temperature_2m']} {units['temperature_2m']}"
    wind = f"{current['wind_speed_10m']} {units['wind_speed_10m']}"
    print(f"{CITY} ({LATITUDE}, {LONGITUDE}): {temp}, wind {wind}")


if __name__ == "__main__":
    main()
