
import requests
import csv
import sys

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

try:
    total = 0

    with open("data/expenses.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")

        for row in reader:
            total += float(row[2])

    rates = {}

    for currency in ["USD", "EUR"]:
        response = requests.get(
            URL,
            params={"valcode": currency, "json": ""},
            timeout=10
        )
        response.raise_for_status()

        data = response.json()
        rates[currency] = data[0]["rate"]
        rate_date = data[0]["exchangedate"]

    print("Лещук Ірина, IT-31")
    print("rate date:", rate_date)
    print(f"total: {total:.2f} UAH")
    print(f"= {total / rates['USD']:.2f} USD")
    print(f"= {total / rates['EUR']:.2f} EUR")

except requests.RequestException as error:
    print(f"Помилка мережі: {error}", file=sys.stderr)
    sys.exit(1)
