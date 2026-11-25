
import requests
import sys

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"


def test_error(mode):
    try:
        if mode == "connection":
            response = requests.get(
                "https://this-domain-does-not-exist-123456.com",
                timeout=10
            )

        elif mode == "http":
            response = requests.get(
                URL + "/wrong-address",
                timeout=10
            )

        elif mode == "timeout":
            response = requests.get(
                "https://httpbin.org/delay/5",
                timeout=0.001
            )

        response.raise_for_status()

    except requests.Timeout:
        print("Помилка: перевищено час очікування", file=sys.stderr)
        sys.exit(1)

    except requests.ConnectionError:
        print("Помилка: немає з'єднання з сервером", file=sys.stderr)
        sys.exit(1)

    except requests.HTTPError as error:
        print(f"Помилка HTTP: {error}", file=sys.stderr)
        sys.exit(1)

    except requests.RequestException as error:
        print(f"Помилка запиту: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Використання: python3 task4.py connection/http/timeout")
        sys.exit(1)

    test_error(sys.argv[1])
