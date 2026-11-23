import requests
import sys

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

tests = {
    "404": ("https://bank.gov.ua/nonexistent-page", 10),
    "timeout": (URL, 0.001),
    "connection": ("https://this-domain-does-not-exist.invalid", 10)
}


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in tests:
        print("Usage: python task4.py 404|timeout|connection")
        sys.exit(1)

    name = sys.argv[1]
    url, timeout = tests[name]

    print(f"Vlad Mushka, IT31")
    print(f"Test: {name}")

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        print("Request successful")

    except requests.RequestException as error:
        print(f"{type(error).__name__}: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
