import sys
import requests

print("Anastasia Zakharchuk, IT-32")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"


def get_rate(code):
    response = requests.get(URL, params={"valcode": code, "json": ""}, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data[0]["rate"], data[0]["exchangedate"]


total = 0
with open("data/expenses.csv", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        total += float(line.split(";")[2])

try:
    usd, date = get_rate("USD")
    eur, _ = get_rate("EUR")
except requests.Timeout:
    print("error: request timed out", file=sys.stderr)
    sys.exit(1)
except requests.ConnectionError:
    print("error: no connection to the server", file=sys.stderr)
    sys.exit(1)
except requests.HTTPError as e:
    print("error: bad status code:", e.response.status_code, file=sys.stderr)
    sys.exit(1)
except requests.RequestException as e:
    print("error:", e, file=sys.stderr)
    sys.exit(1)

print("rate date:", date)
print(f"total: {total:.2f} UAH = {total / usd:.2f} USD = {total / eur:.2f} EUR")
