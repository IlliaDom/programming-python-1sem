from __future__ import annotations

import sys
import requests

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
STUDENT = "Мельник Діана, І-23"


def main() -> int:
    try:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()
        rates = response.json()
    except requests.RequestException as exc:
        print(f"Помилка запиту НБУ: {exc}", file=sys.stderr)
        return 1

    print(STUDENT)
    print("status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type", "невідомо"))
    print("currencies:", len(rates))
    for code in ("USD", "EUR"):
        item = next((rate for rate in rates if rate.get("cc") == code), None)
        if item:
            print(f"{code}: {item['rate']:.4f} UAH (дата: {item['exchangedate']})")
        else:
            print(f"Курс {code} відсутній у відповіді НБУ", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
