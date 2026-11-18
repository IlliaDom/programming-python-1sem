# task4.py
import sys
import requests

def test_request(url, params=None, timeout=10):
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        print("Успіх:", response.status_code)
    except requests.ConnectionError as e:
        print(f"[Помилка зв'язку] Немає інтернету: {e}", file=sys.stderr)
        sys.exit(1)
    except requests.HTTPError as e:
        print(f"[HTTP Помилка] Код стану {e.response.status_code}: {e}", file=sys.stderr)
        sys.exit(1)
    except requests.Timeout as e:
        print(f"[Таймаут] Перевищено час очікування: {e}", file=sys.stderr)
        sys.exit(1)
    except requests.RequestException as e:
        print(f"[Помилка requests]: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    print("--- 1. Тест неіснуючої адреси (404) ---")
    test_request("https://bank.gov.ua/NBUStatService/v1/statdirectory/wrongpath")