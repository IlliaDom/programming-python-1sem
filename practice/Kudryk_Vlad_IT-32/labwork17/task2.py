import csv
import sys
import requests

print("Vlad Kudryk, IT-32")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"


def get_rate(code):
    response = requests.get(URL, params={"json": "", "valcode": code}, timeout=10)
    response.raise_for_status()
    item = response.json()[0]
    return item["rate"], item["exchangedate"]


total = 0
with open("data/expenses.csv", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f, delimiter=";"):
        total += float(row["amount"])

try:
    usd, date = get_rate("USD")
    eur, _ = get_rate("EUR")
except requests.Timeout:
    print("Error: request timed out", file=sys.stderr)
    sys.exit(1)
except requests.ConnectionError:
    print("Error: no internet connection", file=sys.stderr)
    sys.exit(1)
except requests.HTTPError as e:
    print("Error: bad HTTP status:", e, file=sys.stderr)
    sys.exit(1)
except requests.RequestException as e:
    print("Error: request failed:", e, file=sys.stderr)
    sys.exit(1)

print("rate date:", date)
print(f"total: {total:.2f} UAH = {total / usd:.2f} USD = {total / eur:.2f} EUR")