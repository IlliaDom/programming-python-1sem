import sys

import requests

NAME = "Назар, лабораторна 38"  # заміни на своє ім'я та групу
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"


def main() -> int:
    print(NAME)

    try:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"Помилка запиту: {exc}", file=sys.stderr)
        return 1

    rates = response.json()

    print("status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("currencies:", len(rates))

    usd = next((r for r in rates if r["cc"] == "USD"), None)
    eur = next((r for r in rates if r["cc"] == "EUR"), None)

    if usd:
        print(f"USD: {usd['rate']} (на {usd['exchangedate']})")
    else:
        print("USD не знайдено у відповіді", file=sys.stderr)

    if eur:
        print(f"EUR: {eur['rate']} (на {eur['exchangedate']})")
    else:
        print("EUR не знайдено у відповіді", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
