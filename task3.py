
import requests
import sys

URL = "https://api.open-meteo.com/v1/forecast"

CITY = "Lutsk"
LATITUDE = 50.75
LONGITUDE = 25.34


def main():
    try:
        params = {
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "current": "temperature_2m,wind_speed_10m"
        }

        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        current = data["current"]

        print("Воробей Ілля, ІТ-31")
        print(
            f"{CITY} ({LATITUDE}, {LONGITUDE}): "
            f"{current['temperature_2m']} "
            f"{data['current_units']['temperature_2m']}, "
            f"wind {current['wind_speed_10m']} "
            f"{data['current_units']['wind_speed_10m']}"
        )

    except requests.RequestException as error:
        print(f"Помилка мережі: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
