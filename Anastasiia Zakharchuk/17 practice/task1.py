import sys
import requests

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

try:
    response = requests.get(URL, params={"json": ""}, timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Помилка запиту: {e}", file=sys.stderr)
    sys.exit(1)

rates = response.json()

print("Анастасія Захарчук, ІТ-32")
print("status:", response.status_code)
print("Content-Type:", response.headers["Content-Type"])
print("currencies:", len(rates))

for item in rates:
    if item["cc"] in ("USD", "EUR"):
        print(f'{item["cc"]}: {item["rate"]} UAH (дата: {item["exchangedate"]})')