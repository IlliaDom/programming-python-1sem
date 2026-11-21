import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

import requests

NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"

BASE = Path(__file__).resolve().parent
CACHE = BASE / "cache" / "rates.json"
MAX_AGE = timedelta(hours=1)
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"


def load_cache():
    """Повертає (дані, вік) або None, якщо кешу немає чи він застарів."""
    if not CACHE.is_file():
        return None
    try:
        with CACHE.open(encoding="utf-8") as f:
            cached = json.load(f)
        saved_at = datetime.fromisoformat(cached["saved_at"])
        rates = cached["rates"]
    except (ValueError, KeyError):
        return None          # пошкоджений кеш — просто беремо з API
    age = datetime.now() - saved_at
    if age >= MAX_AGE:
        return None
    return rates, age


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    cached = load_cache()
    if cached is not None:
        rates, age = cached
        print(f"source: cache (age {int(age.total_seconds())} s)")
    else:
        try:
            response = requests.get(URL, params={"json": ""}, timeout=10)
            response.raise_for_status()
            rates = response.json()
        except requests.RequestException as e:
            print(f"error: {e}", file=sys.stderr)
            sys.exit(1)
        CACHE.parent.mkdir(exist_ok=True)
        with CACHE.open("w", encoding="utf-8") as f:
            json.dump({"saved_at": datetime.now().isoformat(),
                       "rates": rates}, f, ensure_ascii=False)
        print("source: api (cache saved)")

    print(f"currencies: {len(rates)}")


if __name__ == "__main__":
    main()
