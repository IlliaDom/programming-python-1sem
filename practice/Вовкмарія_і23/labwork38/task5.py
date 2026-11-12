import json
import sys
import time
from pathlib import Path
import requests

API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE_PATH = Path("cache/rates.json")
CACHE_MAX_AGE = 3600

def get_rates():
    if CACHE_PATH.exists():
        try:
            cached = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
            age = int(time.time() - cached["fetched_at"])
            if 0 <= age < CACHE_MAX_AGE:
                return cached["rates"], f"cache (age {age} s)"
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
            pass

    try:
        response = requests.get(API_URL, params={"json": ""}, timeout=10)
        response.raise_for_status()
        rates = response.json()
    except requests.RequestException as exc:
        print(f"Network/API error: {exc}", file=sys.stderr)
        raise SystemExit(1)

    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {"fetched_at": time.time(), "rates": rates}
    CACHE_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return rates, "api (cache saved)"

def main():
    print("Maria Vovk, І-23")
    rates, source = get_rates()
    print("source:", source)
    print("currencies:", len(rates))

if __name__ == "__main__":
    main()
