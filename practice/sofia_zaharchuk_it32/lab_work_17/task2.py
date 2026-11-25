import os
import sys
from pathlib import Path

import requests

NAME, SURNAME, GROUP = "Sofiia", "Zakharchuk", "IT-32"

URL = os.getenv("NBU_URL", "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange")
TIMEOUT = float(os.getenv("HTTP_TIMEOUT", "10"))
EXPENSES = Path(__file__).resolve().parent / "data" / "expenses.csv"


def total_expenses(path: Path) -> float:
    """Sum of the amount column; comments, empty and bad lines are skipped."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        print(f"error: cannot read {path}: {error}", file=sys.stderr)
        sys.exit(1)
    total = 0.0
    for n, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            total += float(line.split(";")[2].replace(",", "."))
        except (ValueError, IndexError):
            print(f"warning: line {n} skipped: {line!r}", file=sys.stderr)
    return total


def get_rate(code: str) -> tuple[float, str]:
    """Official NBU rate for one currency: (rate, date). Handles network errors."""
    try:
        response = requests.get(URL, params={"valcode": code, "json": ""}, timeout=TIMEOUT)
        response.raise_for_status()
        item = response.json()[0]
        return item["rate"], item["exchangedate"]
    except requests.Timeout:
        message = f"the server did not answer in {TIMEOUT} s (timeout)"
    except requests.ConnectionError:
        message = "no connection, check the internet"
    except requests.HTTPError as error:
        message = f"the server answered {error.response.status_code}"
    except (requests.RequestException, IndexError, KeyError):
        message = "the answer has an unexpected format"
    print(f"error: cannot get the {code} rate: {message}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    print(f"{NAME} {SURNAME}, {GROUP}")
    total = total_expenses(EXPENSES)
    usd, date = get_rate("USD")
    eur, _ = get_rate("EUR")
    print(f"rate date: {date}")
    print(f"total: {total:.2f} UAH = {total / usd:.2f} USD = {total / eur:.2f} EUR")


if __name__ == "__main__":
    main()
