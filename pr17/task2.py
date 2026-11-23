import csv
import sys
import requests

NAME = "Nazar Mischuk, IT-32"  

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
TIMEOUT = 10

mode = ""
if len(sys.argv) > 1:
    mode = sys.argv[1]

if mode == "404":
    URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange_wrong"
if mode == "timeout":
    TIMEOUT = 0.001

total_uah = 0
try:
    with open("data/expenses.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_uah = total_uah + float(row["amount"])
except OSError as error:
    print("Не вдалося відкрити expenses.csv:", error, file=sys.stderr)
    sys.exit(1)

rates = {}
rate_date = ""

try:
    for code in ["USD", "EUR"]:
        response = requests.get(
            URL,
            params={"valcode": code, "json": ""},
            timeout=TIMEOUT,
        )
        response.raise_for_status()
        data = response.json()
        rates[code] = data[0]["rate"]
        rate_date = data[0]["exchangedate"]
except requests.Timeout:
    print("Помилка: сервер не відповів вчасно (таймаут)", file=sys.stderr)
    sys.exit(1)
except requests.ConnectionError:
    print("Помилка: немає зʼєднання з інтернетом", file=sys.stderr)
    sys.exit(1)
except requests.HTTPError as error:
    code = error.response.status_code
    if code == 404:
        print("Помилка HTTP 404: такої адреси не існує", file=sys.stderr)
    else:
        print("Помилка HTTP: сервер відповів кодом", code, file=sys.stderr)
    sys.exit(1)
except requests.RequestException as error:
    print("Інша помилка запиту:", error, file=sys.stderr)
    sys.exit(1)
except (ValueError, IndexError, KeyError):
    print("Помилка: відповідь API має неочікуваний вигляд", file=sys.stderr)
    sys.exit(1)

total_usd = total_uah / rates["USD"]
total_eur = total_uah / rates["EUR"]

print(NAME)
print("rate date:", rate_date)
print("USD rate:", rates["USD"], " EUR rate:", rates["EUR"])
print(f"total: {total_uah:.2f} UAH = {total_usd:.2f} USD = {total_eur:.2f} EUR")
