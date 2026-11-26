
import requests
import json
import os
import sys
import time
from datetime import datetime

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
        response = requests.get(
            URL,
            params={"json": ""},
            timeout=10
        )
        response.raise_for_status()

        rates = response.json()

        cache = {
            "timestamp": time.time(),
            "rates": rates
        }

        with open(CACHE_FILE, "w", encoding="utf-8") as file:
            json.dump(cache, file, ensure_ascii=False, indent=4)

        print("source: api (cache saved)")

    print("Лещук Ірина, IT-31")

    for currency in rates:
        if currency["cc"] in ("USD", "EUR"):
            print(
                currency["cc"],
                currency["rate"],
                currency["exchangedate"]
            )

except requests.RequestException as error:
    print(f"Помилка запиту: {error}", file=sys.stderr)
    sys.exit(1)

except (OSError, ValueError, KeyError, TypeError) as error:
    print(f"Помилка роботи з кешем: {error}", file=sys.stderr)
    sys.exit(1)
