import json
import os
import sys
import time
import requests

print("Vlad Kudryk, IT-32")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE = "cache/rates.json"

rates = None

if os.path.exists(CACHE):
    with open(CACHE, encoding="utf-8") as f:
        cached = json.load(f)
    age = time.time() - cached["saved_at"]
    if age < 3600:
        rates = cached["data"]
        print(f"source: cache (age {int(age)} s)")

if rates is None:
    try:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()
        rates = response.json()
    except requests.RequestException as e:
        print("Request error:", e, file=sys.stderr)
        sys.exit(1)
    os.makedirs("cache", exist_ok=True)
    with open(CACHE, "w", encoding="utf-8") as f:
        json.dump({"saved_at": time.time(), "data": rates}, f, ensure_ascii=False)
    print("source: api (cache saved)")