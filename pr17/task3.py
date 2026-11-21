import sys

import requests

NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"
CITY = "Lutsk"
LATITUDE = 50.45
LONGITUDE = 30.52

URL = "https://api.open-meteo.com/v1/forecast"


def main():
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
        current = data["current"]
        units = data["current_units"]
        temp = current["temperature_2m"]
        wind = current["wind_speed_10m"]
    except requests.RequestException as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)
    except (KeyError, ValueError):
        print("error: unexpected response format", file=sys.stderr)
        sys.exit(1)

    print(f"{CITY} ({LATITUDE}, {LONGITUDE}): "
          f"{temp} {units['temperature_2m']}, "
          f"wind {wind} {units['wind_speed_10m']}")


if __name__ == "__main__":
    main()
