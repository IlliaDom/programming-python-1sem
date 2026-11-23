import sys

import requests

print("Oleksandr Romaniuk, IT-31")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

def load_rates(url, params):
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json(), response.status_code, response.headers
    except requests.RequestException:
        sys.stderr.write("Can't get rates")
        sys.exit(1)


if __name__ == "__main__":
    rates, status, headers = load_rates(URL, {"json": ""})

    print("Response code:", status)
    print("Content-Type:", headers["Content-Type"])#
    print("Currencies:", len(rates))

    euro_data = []
    dollar_data = []

    for rate in rates:
        if rate["cc"] == "EUR":
            euro_data.append(rate["cc"])
            euro_data.append(rate["rate"])
            euro_data.append(rate["exchangedate"])
        elif rate["cc"] == "USD":
            dollar_data.append(rate["cc"])
            dollar_data.append(rate["rate"])
            dollar_data.append(rate["exchangedate"])

        continue

    print("Euro:", euro_data[0], euro_data[1], euro_data[2])
    print("Dollar:", dollar_data[0], dollar_data[1], dollar_data[2])