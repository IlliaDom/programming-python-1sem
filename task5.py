
import requests
import sys
import json
import time
from pathlib import Path

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

HERE = Path(__file__).parent
CACHE_DIR = HERE / "cache"
CACHE = CACHE_DIR / "rates.json"

MAX_AGE = 3600


def load_rates():
    CACHE_DIR.mkdir(exist_ok=True)

    if CACHE.exists():
        cached = json.loads(CACHE.read_text(encoding="utf-8"))
        age = time.time() - cached["timestamp"]

        if age < MAX_AGE:
            print(f"source: cache (age {int(age)} s)")
            return cached["rates"]

    response = requests.get(
        URL,
        params={"json": ""},
        timeout=10
    )
    response.raise_for_status()

    data = response.json()

    rates = {
        item["cc"]: item["rate"]
        for item in data
    }

    cached = {
        "timestamp": time.time(),
        "rates": rates
    }

    CACHE.write_text(
        json.dumps(cached, ensure_ascii=False, indent=4),
        encoding="utf-8"
    )

    print("source: api (cache saved)")

    return rates


def main():
    try:
        print("Воробей Ілля, ІТ-31")

        rates = load_rates()

        print("USD:", rates["USD"])
        print("EUR:", rates["EUR"])

    except requests.RequestException as error:
        print(f"Помилка мережі: {error}", file=sys.stderr)
        sys.exit(1)

    except (OSError, ValueError, KeyError) as error:
        print(f"Помилка кешу або даних: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
