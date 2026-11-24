from pathlib import Path
import requests
import json
from datetime import datetime
path = Path(__file__).resolve().parent / "data" / "expenses.json"
with open(path) as f:
    expenses = json.load(f)
params = {"json": "", "valcode": "USD"}
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
response = requests.get(URL, params = params, timeout=10)
dollar = response.json()[0]["rate"]

params = {"json": "", "valcode": "EUR"}
response = requests.get(URL, params = params, timeout=10)
euro = response.json()[0]["rate"]

full_expenses = 0
for i in range(0, len(expenses)):
    full_expenses += expenses[i]["amount"]


print(datetime.now().strftime("%d.%m.%Y"))
print(f"total: {full_expenses}UAH = {round(full_expenses/dollar,2)}USD = {round(full_expenses/euro, 2)}EUR")