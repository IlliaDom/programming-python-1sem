from pathlib import Path
import requests
import json
from datetime import datetime
import sys
try:
    path = Path(__file__).resolve().parent / "data" / "expenses.json"
    with open(path) as f:
        expenses = json.load(f)
    params = {"json": "", "valcode": "USD"}
    URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
    response = requests.get(URL, params = params, timeout=0.1)
    response.raise_for_status()
    dollar = response.json()[0]["rate"]

    params = {"json": "", "valcode": "EUR"}
    response = requests.get(URL, params = params, timeout=0.1)
    response.raise_for_status()
    euro = response.json()[0]["rate"]


    full_expenses = 0
    for i in range(0, len(expenses)):
        full_expenses += expenses[i]["amount"]


    print(datetime.now().strftime("%d.%m.%Y"))
    print(f"total: {full_expenses}UAH = {round(full_expenses/dollar,2)}USD = {round(full_expenses/euro, 2)}EUR")
except requests.Timeout:
    sys.exit("Time of waiting is out")
except requests.ConnectionError:
    sys.exit("Connection Error")
except requests.HTTPError as error:
    sys.exit("Не існуюча адреса")
