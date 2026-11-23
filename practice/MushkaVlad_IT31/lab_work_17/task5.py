import json
import requests
import sys
import time
from pathlib import Path

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE = Path("cache/rates.json")
CACHE_MAX_AGE = 3600


def get_rates():
    if CACHE.exists():
        try:
            data = json.loads(CACHE.read_text(encoding="utf-8"))

            if time.time() - data["timestamp"] < CACHE_MAX_AGE:
                print("Source: cache")
                return data["rates"]

        except (ValueError, KeyError, OSError):
            pass

    try:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()
        rates = response.json()

        CACHE.parent.mkdir(parents=True, exist_ok=True)
        CACHE.write_text(
            json.dumps({
                "timestamp": time.time(),
                "rates": rates
            }, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

        print("Source: API (cache updated)")
        return rates

    except requests.RequestException as error:
        print(f"Request error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    print("Vlad Mushka, IT31")

    rates = get_rates()

    for code in ("USD", "EUR"):
        rate = next(item for item in rates if item["cc"] == code)
        print(f'{code}: {rate["rate"]} UAH')
