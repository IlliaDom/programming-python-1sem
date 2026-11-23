import sys
import requests

print("Vlad Kudryk, IT-32")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

try:
    response = requests.get(URL, params={"json": ""}, timeout=10)
    response.raise_for_status()
    rates = response.json()
except requests.RequestException as e:
    print("Request error:", e, file=sys.stderr)
    sys.exit(1)

print("status:", response.status_code)
print("content-type:", response.headers["Content-Type"])
print("currencies:", len(rates))

for item in rates:
    if item["cc"] in ("USD", "EUR"):
        print(item["cc"], item["rate"], "date:", item["exchangedate"])