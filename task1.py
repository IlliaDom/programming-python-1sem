
import requests
import sys

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"


def main():
    try:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()

        rates = response.json()

        print("Воробей Ілля, ІТ-21")
        print("status:", response.status_code)
        print("Content-Type:", response.headers.get("Content-Type"))
        print("currencies:", len(rates))

        for currency in ("USD", "EUR"):
            item = next(rate for rate in rates if rate["cc"] == currency)
            print(
                item["cc"],
                item["rate"],
                "UAH",
                "date:",
                item["exchangedate"]
            )

    except requests.RequestException as error:
        print(f"Помилка мережі: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
