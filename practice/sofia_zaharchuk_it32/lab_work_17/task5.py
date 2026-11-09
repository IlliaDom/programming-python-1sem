import json
import sys
import time
from pathlib import Path

import requests

NAME, SURNAME, GROUP = "Sofiia", "Zakharchuk", "IT-32"

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE = Path(__file__).resolve().parent / "cache" / "rates.json"
MAX_AGE = 3600  # секунд


def read_cache() -> tuple[list, int] | None:
    """Return (rates, age in seconds) if the cache is fresh, otherwise None."""
    if not CACHE.exists():
        return None
    try:
        saved = json.loads(CACHE.read_text(encoding="utf-8"))
        age = int(time.time() - saved["saved_at"])
        if 0 <= age < MAX_AGE:
            return saved["rates"], age
    except (json.JSONDecodeError, KeyError, TypeError):
        pass  # пошкоджений кеш просто ігноруємо і беремо дані з API
    return None


def fetch_rates() -> list:
    try:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()
        rates = response.json()
    except requests.RequestException as error:
        print(f"error: cannot get rates: {error}", file=sys.stderr)
        sys.exit(1)
    CACHE.parent.mkdir(exist_ok=True)
    saved = {"saved_at": time.time(), "rates": rates}
    CACHE.write_text(json.dumps(saved, indent=2, ensure_ascii=False), encoding="utf-8")
    return rates


def main() -> None:
    print(f"{NAME} {SURNAME}, {GROUP}")
    cached = read_cache()
    if cached:
        rates, age = cached
        print(f"source: cache (age {age} s)")
    else:
        rates = fetch_rates()
        print("source: api (cache saved)")
    for code in ("USD", "EUR"):
        item = next((r for r in rates if r["cc"] == code), None)
        if item:
            print(f"{code}: {item['rate']} UAH (date {item['exchangedate']})")


if __name__ == "__main__":
    main()
