from __future__ import annotations

import sys
import requests

STUDENT = "Мельник Діана, І-23"
CITY = "Олика"
LATITUDE = 50.72272
LONGITUDE = 25.81208
URL = "https://api.open-meteo.com/v1/forecast"


def main() -> int:
    try:
        response = requests.get(
            URL,
            params={
                "latitude": LATITUDE,
                "longitude": LONGITUDE,
                "current": "temperature_2m,wind_speed_10m",
            },
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        current = data["current"]
        units = data.get("current_units", {})
    except requests.RequestException as exc:
        print(f"Помилка запиту Open-Meteo: {exc}", file=sys.stderr)
        return 1
    except (ValueError, KeyError, TypeError) as exc:
        print(f"Не вдалося прочитати відповідь погоди: {exc}", file=sys.stderr)
        return 1

    print(STUDENT)
    print(f"{CITY} ({LATITUDE:.5f}, {LONGITUDE:.5f}): "
          f"{current['temperature_2m']} {units.get('temperature_2m', '°C')}, "
          f"wind {current['wind_speed_10m']} {units.get('wind_speed_10m', 'km/h')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
