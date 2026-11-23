import csv
import requests
import sys
from decimal import Decimal
from pathlib import Path

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

try:
    with Path("data/expenses.csv").open(encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]
        header = lines[0].lstrip("# ").split(";")
        rows = csv.DictReader(lines[1:], fieldnames=header, delimiter=";")
        total = sum(Decimal(row["amount"]) for row in rows)

    rates = {}

    for code in ("USD", "EUR"):
        response = requests.get(
            URL,
            params={"valcode": code, "json": ""},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        rates[code] = data[0]

except requests.RequestException as error:
    print(f"Network error: {error}", file=sys.stderr)
    sys.exit(1)
except (OSError, KeyError, IndexError, ValueError) as error:
    print(f"Data error: {error}", file=sys.stderr)
    sys.exit(1)

print("Vlad Mushka, IT31")
print("rate date:", rates["USD"]["exchangedate"])
print(f"total: {total:.2f} UAH")

for code in ("USD", "EUR"):
    converted = total / Decimal(str(rates[code]["rate"]))
    print(f"       = {converted:.2f} {code}")
