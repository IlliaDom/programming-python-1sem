import requests
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
response = requests.get(URL, params = {"json":""}, timeout=10)
response.raise_for_status()
rates = response.json()
print(response.status_code)
print("валют:", len(rates))
euro = ""
euro_date = ""
dollar = ""
dollar_date = ""
for rate in rates:
    if rate["cc"] == "EUR":
        euro = rate["rate"]
        euro_date = rate["exchangedate"]
    elif rate["cc"] == "USD":
        dollar = rate["rate"]
        dollar_date = rate["exchangedate"]
print(f"Курс євро: {euro}. Дата: {euro_date}")
print(f"Курс долара: {dollar}. Дата: {dollar_date}")
