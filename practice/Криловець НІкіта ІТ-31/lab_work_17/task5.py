import json
import requests
import sys
import os
import time

print("Nikita Krilovets, IT-31")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE_FILE = "cache/rates.json"

try:
    os.makedirs("cache", exist_ok=True)

    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as file:
            cache = json.load(file)

        age = time.time() - cache["timestamp"]

        if age < 3600:
            rates = cache["rates"]
            print(f"source: cache (age {int(age)} s)")

        else:
            rates = None
    else:
        rates = None

    if rates is None:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()

        rates = response.json()

        cache = {
            "timestamp": time.time(),
            "rates": rates
        }

        with open(CACHE_FILE, "w", encoding="utf-8") as file:
            json.dump(cache, file, indent=2, ensure_ascii=False)

        print("source: api (cache saved)")

except (requests.RequestException, OSError, ValueError, KeyError, TypeError) as error:
    print(error, file=sys.stderr)
    sys.exit(1)
