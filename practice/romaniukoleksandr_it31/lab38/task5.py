import time
import json
import sys
from pathlib import Path

import requests

print("Oleksandr Romaniuk, IT-31")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE = Path(__file__).parent / "cache/rates.json"
MAX_AGE = 3600

def load_exchange_rate():
    if CACHE.exists() and time.time() - CACHE.stat().st_mtime < MAX_AGE:
        print(f"source: cache(age {round(time.time() - CACHE.stat().st_mtime)} s)")
        return json.loads(CACHE.read_text(encoding="utf-8"))
    try:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        sys.stderr.write("Can't get rates")
        sys.exit(1)

    rates = response.json()
    CACHE.parent.mkdir(exist_ok=True)
    CACHE.write_text(json.dumps(rates, indent=2, ensure_ascii=False), encoding="utf-8")
    print("source: api(cache saved)")


if __name__ == "__main__":
    load_exchange_rate()