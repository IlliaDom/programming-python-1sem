# task2.py
import csv
import sys
import requests

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

total_uah = 0.0
try:
    with open("data/expenses.csv", mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_uah += float(row["amount_uah"])
except FileNotFoundError:
    print("Помилка: файл data/expenses.csv не знайдено!", file=sys.stderr)
    sys.exit(1)

try:
    res_usd = requests.get(URL, params={"valcode": "USD", "json": ""}, timeout=10)
    res_usd.raise_for_status()
    usd_data = res_usd.json()[0]

    res_eur = requests.get(URL, params={"valcode": "EUR", "json": ""}, timeout=10)
    res_eur.raise_for_status()
    eur_data = res_eur.json()[0]
except requests.RequestException as e:
    print(f"Помилка отримання курсів: {e}", file=sys.stderr)
    sys.exit(1)

rate_date = usd_data["exchangedate"]
rate_usd = usd_data["rate"]
rate_eur = eur_data["rate"]

total_usd = total_uah / rate_usd
total_eur = total_uah / rate_eur

print("Батура Каріна Віталіївна, ІТ-31")
print(f"rate date: {rate_date}")
print(f"total: {total_uah:.2f} UAH = {total_usd:.2f} USD = {total_eur:.2f} EUR")