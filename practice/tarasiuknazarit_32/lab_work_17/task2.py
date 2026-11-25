import csv
import sys

import requests

NAME = "Назар, лабораторна 38"  # заміни на своє ім'я та групу
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
EXPENSES_FILE = "data/expenses.csv"


def get_total_uah(path: str) -> float:
    total = 0.0
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += float(row["amount"])
    return total


def get_rate(valcode: str) -> tuple[float, str]:
    """Повертає (курс, дата) для заданого коду валюти."""
    response = requests.get(
        URL, params={"json": "", "valcode": valcode}, timeout=10
    )
    response.raise_for_status()
    data = response.json()
    if not data:
        raise ValueError(f"Валюту {valcode} не знайдено у відповіді НБУ")
    return data[0]["rate"], data[0]["exchangedate"]


def main() -> int:
    print(NAME)

    try:
        total_uah = get_total_uah(EXPENSES_FILE)
        usd_rate, rate_date = get_rate("USD")
        eur_rate, _ = get_rate("EUR")
    except FileNotFoundError:
        print(f"Файл {EXPENSES_FILE} не знайдено", file=sys.stderr)
        return 1
    except requests.RequestException as exc:
        print(f"Помилка запиту до НБУ: {exc}", file=sys.stderr)
        return 1

    total_usd = total_uah / usd_rate
    total_eur = total_uah / eur_rate

    print(f"rate date: {rate_date}")
    print(
        f"total: {total_uah:.2f} UAH = {total_usd:.2f} USD = {total_eur:.2f} EUR"
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
