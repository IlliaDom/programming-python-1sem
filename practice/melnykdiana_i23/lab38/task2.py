from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
import requests

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
STUDENT = "Мельник Діана, І-23"
DATA = Path(__file__).with_name("expenses.csv")


def fetch_rate(code: str, *, timeout: float = 10, url: str = URL) -> tuple[float, str]:
    response = requests.get(url, params={"valcode": code, "json": ""}, timeout=timeout)
    response.raise_for_status()
    data = response.json()
    if not data:
        raise ValueError(f"НБУ не повернув курс {code}")
    return float(data[0]["rate"]), data[0]["exchangedate"]


def total_expenses() -> float:
    with DATA.open("r", encoding="utf-8-sig", newline="") as file:
        rows = csv.DictReader(file)
        return sum(float(row["amount"]) for row in rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Витрати у гривнях, доларах і євро")
    parser.add_argument("--demo-error", choices=("connection", "http", "timeout"), help="відтворити помилку для завдання 4")
    args = parser.parse_args()
    try:
        if args.demo_error == "connection":
            # Reserved non-routable address: демонстрація відсутності з'єднання.
            usd, date = fetch_rate("USD", url="http://10.255.255.1", timeout=10)
            eur, _ = fetch_rate("EUR", url="http://10.255.255.1", timeout=10)
        elif args.demo_error == "http":
            usd, date = fetch_rate("USD", url="https://bank.gov.ua/NBUStatService/no-such-path")
            eur, _ = fetch_rate("EUR", url="https://bank.gov.ua/NBUStatService/no-such-path")
        elif args.demo_error == "timeout":
            usd, date = fetch_rate("USD", timeout=0.001)
            eur, _ = fetch_rate("EUR", timeout=0.001)
        else:
            usd, date = fetch_rate("USD")
            eur, eur_date = fetch_rate("EUR")
            if eur_date != date:
                print(f"Увага: дати курсів відрізняються: USD {date}, EUR {eur_date}", file=sys.stderr)

        total = total_expenses()
        print(STUDENT)
        print(f"rate date: {date}")
        print(f"total: {total:.2f} UAH = {total / usd:.2f} USD = {total / eur:.2f} EUR")
        return 0
    except requests.ConnectionError as exc:
        print(f"Помилка з'єднання з API: {exc}", file=sys.stderr)
    except requests.Timeout as exc:
        print(f"Час очікування відповіді вичерпано: {exc}", file=sys.stderr)
    except requests.HTTPError as exc:
        print(f"HTTP-помилка відповіді API: {exc}", file=sys.stderr)
    except (requests.RequestException, ValueError, KeyError, OSError, csv.Error) as exc:
        print(f"Не вдалося отримати або обробити дані: {exc}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
