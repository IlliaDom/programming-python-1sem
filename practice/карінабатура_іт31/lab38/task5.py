# task5.py
import json
import os
import sys
import time
import requests

CACHE_FILE = "cache/rates.json"
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
ONE_HOUR = 3600

def get_rates():
    now = time.time()
    if os.path.exists(CACHE_FILE):
        file_mtime = os.path.getmtime(CACHE_FILE)
        age = int(now - file_mtime)
        if age < ONE_HOUR:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data, f"cache (age {age} s)"

    try:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
        with open(CACHE_FILE, "w", encoding="utf-8`") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        return data, "api (cache saved)"
    except requests.RequestException as e:
        print(f"Помилка мережі: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    print("Батура Каріна Віталіївна, ІТ-31")
    rates, source = get_rates()
    print(f"source: {source}")
    print(f"Загалом завантажено курсів: {len(rates)}")