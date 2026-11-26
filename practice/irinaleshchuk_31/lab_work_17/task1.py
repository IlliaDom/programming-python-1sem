
import requests
import sys

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

try:
    response = requests.get(URL, params={"json": ""}, timeout=10)
    response.raise_for_status()

    rates = response.json()

    print("Лещук Ірина, IT-31")
    print("status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("currencies:", len(rates))

    for currency in rates:
        if currency["cc"] in ("USD", "EUR"):
            print(
                currency["cc"],
                currency["rate"],
                currency["exchangedate"]
            )

except requests.RequestException as error:
    print(f"Помилка запиту: {error}", file=sys.stderr)
    sys.exit(1)
