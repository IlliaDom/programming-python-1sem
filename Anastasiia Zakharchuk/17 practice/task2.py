import csv
import sys
import requests

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CSV_PATH = "data/expenses.csv"
AMOUNT_COLUMN = "amount"  # поміняй на назву колонки із сумою у твоєму файлі


def get_rate(code):
    """Повертає (курс, дата) для валюти з окремого запиту."""
    try:
        response = requests.get(
            URL, params={"valcode": code, "json": ""}, timeout=10
        )
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Помилка запиту ({code}): {e}", file=sys.stderr)
        sys.exit(1)
    data = response.json()
    return data[0]["rate"], data[0]["exchangedate"]


def read_total(path):
    total = 0.0
    names = ["date", "category", "amount", "note"]
    with open(path, encoding="utf-8", newline="") as f:
        lines = (
            line for line in f
            if line.strip() and not line.startswith("#")
        )
        for row in csv.DictReader(lines, fieldnames=names, delimiter=";"):
            total += float(row["amount"])
    return total


total_uah = read_total(CSV_PATH)
usd_rate, rate_date = get_rate("USD")
eur_rate, _ = get_rate("EUR")

print("Анастасія Захарчук, ІТ-32")
print("rate date:", rate_date)
print(
    f"total: {total_uah:.2f} UAH = {total_uah / usd_rate:.2f} USD "
    f"= {total_uah / eur_rate:.2f} EUR"
)