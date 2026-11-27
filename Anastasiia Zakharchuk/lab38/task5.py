import json
import os
import sys
import time
import requests

print("Anastasia Zakharchuk, IT-32")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE_FILE = "cache/rates.json"
MAX_AGE = 3600

rates = None

if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, encoding="utf-8") as f:
            cache = json.load(f)
        age = time.time() - cache["time"]
        if age < MAX_AGE:
            rates = cache["data"]
            print(f"source: cache (age {int(age)} s)")
    except (json.JSONDecodeError, KeyError):
        rates = None

if rates is None:
    try:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()
        rates = response.json()
    except requests.RequestException as e:
        print("request error:", e, file=sys.stderr)
        sys.exit(1)
    os.makedirs("cache", exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump({"time": time.time(), "data": rates}, f, ensure_ascii=False)
    print("source: api (cache saved)")

print("currencies:", len(rates))
