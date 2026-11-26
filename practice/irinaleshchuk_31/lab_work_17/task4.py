
import requests
import sys

print("Лещук Ірина, IT-31")

# 1. Помилка з'єднання
try:
    requests.get("http://127.0.0.1:1", timeout=10)
except requests.ConnectionError:
    print("ConnectionError: немає з'єднання", file=sys.stderr)

# 2. Помилка HTTP 404
try:
    response = requests.get(
        "https://httpbin.org/status/404",
        timeout=10
    )
    response.raise_for_status()
except requests.HTTPError:
    print("HTTPError: помилка 404", file=sys.stderr)

# 3. Помилка таймауту
try:
    requests.get(
        "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange",
        timeout=0.001
    )
except requests.Timeout:
    print("Timeout: час очікування вичерпано", file=sys.stderr)

print("Перевірку трьох помилок завершено.")
sys.exit(1)
