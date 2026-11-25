import json
import sys
import time
from pathlib import Path

import requests

NAME = "Назар, лабораторна 38"  # заміни на своє ім'я та групу
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE_PATH = Path("cache/rates.json")
CACHE_TTL_SECONDS = 60 * 60  # 1 година


def load_from_cache() -> tuple[list, float] | None:
    if not CACHE_PATH.exists():
        return None
    try:
        with CACHE_PATH.open(encoding="utf-8") as f:
            payload = json.load(f)
        return payload["rates"], payload["fetched_at"]
    except (json.JSONDecodeError, KeyError):
        return None


def save_to_cache(rates: list) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {"rates": rates, "fetched_at": time.time()}
    with CACHE_PATH.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)


def fetch_from_api() -> list:
    response = requests.get(URL, params={"json": ""}, timeout=10)
    response.raise_for_status()
    return response.json()


def main() -> int:
    print(NAME)

    cached = load_from_cache()

    if cached is not None:
        rates, fetched_at = cached
        age = time.time() - fetched_at
        if age < CACHE_TTL_SECONDS:
            print(f"source: cache (age {age:.0f} s)")
            print("currencies:", len(rates))
            return 0

    try:
        rates = fetch_from_api()
    except requests.RequestException as exc:
        print(f"Помилка запиту: {exc}", file=sys.stderr)
        return 1

    save_to_cache(rates)
    print("source: api (cache saved)")
    print("currencies:", len(rates))

    return 0


if __name__ == "__main__":
    sys.exit(main())
