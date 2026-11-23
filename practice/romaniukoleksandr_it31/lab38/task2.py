import sys
from pathlib import Path

import requests

print("Oleksandr Romaniuk, IT-31")

expenses = Path("data/expenses.csv")
data = []

with open(expenses, "r", encoding="utf-8") as f:
    for record in f.readlines():
        if record.startswith("#") or record == "":
            continue

        data.append(record.strip().split(";"))

total_gryvnia = 0

for record in data:
    total_gryvnia += float(record[2])

def process_errors(url, params):
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.ConnectionError:
        print("Bad connection. Please connect to Internet", file=sys.stderr)
        sys.exit(1)
    except requests.HTTPError as err:
        print(f"Server answered {err.response.status_code}", file=sys.stderr)
        sys.exit(1)
    except requests.Timeout:
        print("Server is too slow(not answered in 10 seconds)", file=sys.stderr)
        sys.exit(1)

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

euro_info = process_errors(URL, {"json": "", "valcode": "EUR"})
euro_rate = euro_info[0]["rate"]

dollar_info = process_errors(URL, {"json": "", "valcode": "USD"})
dollar_rate = dollar_info[0]["rate"]

total_euro = total_gryvnia / euro_rate
total_dollar = total_gryvnia / dollar_rate

print("rate date(EUR, USD):", euro_info[0]["exchangedate"], dollar_info[0]["exchangedate"])
print(f"total: {total_gryvnia:.2f} UAH = {total_euro:.2f} EUR = {total_dollar:.2f} USD")

