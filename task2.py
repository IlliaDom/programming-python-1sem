
import requests
import sys
from pathlib import Path

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

HERE = Path(__file__).parent
EXPENSES = HERE / "data" / "expenses.csv"


def get_rate(currency):
    response = requests.get(
        URL,
        params={"valcode": currency, "json": ""},
        timeout=10
    )
    response.raise_for_status()

    data = response.json()
    return data[0]["rate"], data[0]["exchangedate"]


def get_total():
    if not EXPENSES.exists():
        raise FileNotFoundError(f"Файл не знайдено: {EXPENSES}")

    total = 0.0

    for line in EXPENSES.read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.startswith("#"):
            try:
                total += float(line.split(";")[2].strip())
            except (ValueError, IndexError):
                continue

    return total


def main():
    try:
        total = get_total()

        usd, date = get_rate("USD")
        eur, eur_date = get_rate("EUR")

        print("Воробей Ілля, ІТ-21")
        print("rate date:", date)
        print(f"total: {total:.2f} UAH")
        print(f"USD: {total / usd:.2f}")
        print(f"EUR: {total / eur:.2f}")

    except requests.RequestException as error:
        print(f"Помилка запиту: {error}", file=sys.stderr)
        sys.exit(1)

    except (OSError, ValueError) as error:
        print(f"Помилка файлу або даних: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
