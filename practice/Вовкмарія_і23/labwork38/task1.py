import requests
import sys

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

def main():
    try:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()
        rates = response.json()
    except requests.RequestException as exc:
        print(f"Network/API error: {exc}", file=sys.stderr)
        raise SystemExit(1)

    print("Maria Vovk, І-23")
    print("status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type", "unknown"))
    print("currencies:", len(rates))
    for code in ("USD", "EUR"):
        item = next((rate for rate in rates if rate.get("cc") == code), None)
        if item:
            print(f"{code}: {item['rate']:.4f} UAH, date: {item['exchangedate']}")
        else:
            print(f"{code}: not found")

if __name__ == "__main__":
    main()
