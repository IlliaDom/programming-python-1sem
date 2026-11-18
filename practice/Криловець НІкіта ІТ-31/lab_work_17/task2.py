import csv
import requests
import sys

print("Nikita Krilovets, IT-31")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

try:
    total = 0

    with open("data/expenses.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        reader.fieldnames = [
            name.lstrip("# ").strip() for name in reader.fieldnames
        ]

        for row in reader:
            total += float(row["amount"])

    usd_response = requests.get(
        URL,
        params={"valcode": "USD", "json": ""},
        timeout=10
    )
    usd_response.raise_for_status()
    usd = usd_response.json()[0]

    eur_response = requests.get(
        URL,
        params={"valcode": "EUR", "json": ""},
        timeout=10
    )
    eur_response.raise_for_status()
    eur = eur_response.json()[0]

    usd_total = total / usd["rate"]
    eur_total = total / eur["rate"]

    print("rate date:", usd["exchangedate"])
    print(f"total: {total:.2f} UAH = {usd_total:.2f} USD = {eur_total:.2f} EUR")

except (requests.RequestException, OSError, KeyError, ValueError, IndexError) as error:
    print(error, file=sys.stderr)
    sys.exit(1)
