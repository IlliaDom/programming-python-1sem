import csv
import sys

import requests

NAME = "Назар, лабораторна 38"  # заміни на своє ім'я та групу
BASE_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
WRONG_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/NOPE"
EXPENSES_FILE = "data/expenses.csv"


def get_total_uah(path: str) -> float:
    total = 0.0
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += float(row["amount"])
    return total


def get_rate(valcode: str, url: str = BASE_URL, timeout: float = 10) -> tuple[float, str]:
    response = requests.get(
        url, params={"json": "", "valcode": valcode}, timeout=timeout
    )
    response.raise_for_status()
    data = response.json()
    if not data:
        raise ValueError(f"Валюту {valcode} не знайдено у відповіді НБУ")
    return data[0]["rate"], data[0]["exchangedate"]


def run(scenario: str) -> int:
    url = BASE_URL
    timeout = 10.0

    if scenario == "not_found":
        url = WRONG_URL
    elif scenario == "timeout":
        timeout = 0.001
    # "no_internet" використовує звичайні url/timeout — вимкни Wi-Fi вручну

    try:
        total_uah = get_total_uah(EXPENSES_FILE)
        usd_rate, rate_date = get_rate("USD", url=url, timeout=timeout)
        eur_rate, _ = get_rate("EUR", url=url, timeout=timeout)
    except requests.ConnectionError:
        print("Немає з'єднання з інтернетом", file=sys.stderr)
        return 1
    except requests.HTTPError as exc:
        print(f"Сервер повернув помилку: {exc}", file=sys.stderr)
        return 1
    except requests.Timeout:
        print("Перевищено час очікування відповіді (timeout)", file=sys.stderr)
        return 1
    except requests.RequestException as exc:
        print(f"Помилка запиту: {exc}", file=sys.stderr)
        return 1

    total_usd = total_uah / usd_rate
    total_eur = total_uah / eur_rate

    print(f"rate date: {rate_date}")
    print(
        f"total: {total_uah:.2f} UAH = {total_usd:.2f} USD = {total_eur:.2f} EUR"
    )
    return 0


def main() -> int:
    print(NAME)
    scenario = sys.argv[1] if len(sys.argv) > 1 else "ok"
    return run(scenario)


if __name__ == "__main__":
    sys.exit(main())
