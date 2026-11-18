# task1.py
import sys
import requests

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

try:
    response = requests.get(URL, params={"json": ""}, timeout=10)
    response.raise_for_status()
    rates = response.json()
except requests.RequestException as e:
    print(f"Помилка мережі: {e}", file=sys.stderr)
    sys.exit(1)

print("status:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("currencies:", len(rates))

for item in rates:
    if item.get("cc") in ("USD", "EUR"):
        print(f"Валюта: {item['cc']}, Курс: {item['rate']} UAH, Дата: {item['exchangedate']}")