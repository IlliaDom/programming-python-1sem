# Завдання 5. Кеш відповіді НБУ (діє 1 годину)
import json
import os
import sys
import time
import requests

NAME = "Nazar Mischuk, IT-32"  

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE_FILE = "cache/rates.json"
MAX_AGE = 3600  # одна година у секундах

rates = None
source = ""
age = 0

# 1. Пробуємо прочитати кеш
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, encoding="utf-8") as file:
            cached = json.load(file)
        age = time.time() - cached["saved_at"]
        if age < MAX_AGE:
            rates = cached["data"]
            source = f"cache (age {int(age)} s)"
    except (OSError, ValueError, KeyError):
        # якщо кеш зіпсований - просто ігноруємо його
        print("Кеш пошкоджено, роблю новий запит", file=sys.stderr)

# 2. Якщо кешу немає або він старий - йдемо в API
if rates is None:
    try:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()
        rates = response.json()
    except requests.RequestException as error:
        print("Помилка запиту:", error, file=sys.stderr)
        sys.exit(1)

    # зберігаємо відповідь разом з часом отримання
    os.makedirs("cache", exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as file:
        json.dump({"saved_at": time.time(), "data": rates}, file, ensure_ascii=False)
    source = "api (cache saved)"

print(NAME)
print("source:", source)
print("currencies:", len(rates))
