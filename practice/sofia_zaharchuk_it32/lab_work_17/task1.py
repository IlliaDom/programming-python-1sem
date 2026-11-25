import sys

import requests

NAME, SURNAME, GROUP = "Sofiia", "Zakharchuk", "IT-32"

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"


def main() -> None:
    print(f"{NAME} {SURNAME}, {GROUP}")
    try:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()
        rates = response.json()
    except requests.RequestException as error:
        print(f"error: {error}", file=sys.stderr)
        sys.exit(1)

    print("status:", response.status_code)
    print("content-type:", response.headers.get("Content-Type"))
    print("currencies:", len(rates))
    for code in ("USD", "EUR"):
        item = next((r for r in rates if r["cc"] == code), None)
        if item is None:
            print(f"{code}: not found in the answer")
        else:
            print(f"{code}: {item['rate']} UAH (date {item['exchangedate']})")


if __name__ == "__main__":
    main()
