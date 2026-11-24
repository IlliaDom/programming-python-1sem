import requests
from pathlib import Path
import json
from datetime import datetime, timedelta
path = Path(__file__).resolve().parent/"cache"/"rates.json"
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
if not path.exists():
    with open(path, "w", encoding="utf-8") as f:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response = response.json()
        cache = {
            "last_cache": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "rates": response
        }
        json.dump(cache, f, ensure_ascii=False, indent=4)

with open(path, "r", encoding="utf-8") as f:
    cache = json.load(f)
last_cache = datetime.strptime(cache["last_cache"], "%Y-%m-%d %H:%M")
print(last_cache)
if path.exists():
    if datetime.now() - timedelta(hours = 1) >= last_cache:
        with open(path, "w", encoding="utf-8") as f:
            response = requests.get(URL, params={"json": ""}, timeout=10)
            response = response.json()
            cache = {
                "last_cache": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "rates": response
            }
            json.dump(cache, f, ensure_ascii=False, indent=4)
