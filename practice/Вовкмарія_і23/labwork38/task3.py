import requests
import sys

URL = "https://api.open-meteo.com/v1/forecast"
CITY = "Volodymyr"
LATITUDE = 50.842173
LONGITUDE = 24.3191015

def main():
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current": "temperature_2m,wind_speed_10m",
        "timezone": "Europe/Kyiv"
    }
    try:
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as exc:
        print(f"Network/API error: {exc}", file=sys.stderr)
        raise SystemExit(1)

    current = data["current"]
    units = data.get("current_units", {})
    print("Maria Vovk, І-23")
    print(f"{CITY} ({LATITUDE}, {LONGITUDE}): "
          f"{current['temperature_2m']} {units.get('temperature_2m', '°C')}, "
          f"wind {current['wind_speed_10m']} {units.get('wind_speed_10m', 'km/h')}")

if __name__ == "__main__":
    main()
