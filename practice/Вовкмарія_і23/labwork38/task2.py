import argparse
import csv
import sys
import requests

API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CSV_PATH = "data/expenses.csv"

def total_expenses():
    total = 0.0
    with open(CSV_PATH, "r", encoding="utf-8-sig", newline="") as file:
        for row in csv.DictReader(file, delimiter=";"):
            total += float(row["amount"])
    return total

def get_rate(code, demo=None):
    url = API_URL
    params = {"valcode": code, "json": ""}
    timeout = 10

    if demo == "connection":
        url = "https://this-domain-does-not-exist.invalid/"
        params = None
    elif demo == "http":
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/not-found"
        params = None
    elif demo == "timeout":
        timeout = 0.001

    response = requests.get(url, params=params, timeout=timeout)
    response.raise_for_status()
    data = response.json()
    if not data:
        raise ValueError(f"No rate returned for {code}")
    return data[0]

def main():
    parser = argparse.ArgumentParser(description="Convert personal expenses using NBU rates.")
    parser.add_argument("--demo", choices=("connection", "http", "timeout"),
                        help="demonstrate one of the required request errors")
    args = parser.parse_args()

    print("Maria Vovk, І-23")
    try:
        if args.demo:
            get_rate("USD", demo=args.demo)
            return
        total = total_expenses()
        usd = get_rate("USD")
        eur = get_rate("EUR")
        print("rate date:", usd["exchangedate"])
        print(f"total: {total:.2f} UAH = {total / float(usd['rate']):.2f} USD = {total / float(eur['rate']):.2f} EUR")
    except requests.RequestException as exc:
        print(f"Request failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Data error: {exc}", file=sys.stderr)
        raise SystemExit(1)

if __name__ == "__main__":
    main()
