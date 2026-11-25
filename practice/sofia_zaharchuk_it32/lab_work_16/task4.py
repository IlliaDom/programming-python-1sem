import json
import sys
from datetime import date
from pathlib import Path

NAME, SURNAME, GROUP = "Sofiia", "Zakharchuk", "IT-32"

BASE = Path(__file__).resolve().parent
EXPENSES = BASE / "data" / "expenses.json"


def dates_to_str(value):
    """Recursively turn every date into an ISO string."""
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: dates_to_str(v) for k, v in value.items()}
    if isinstance(value, list):
        return [dates_to_str(v) for v in value]
    return value


def str_to_dates(value):
    """Recursively turn ISO date strings (YYYY-MM-DD) back into date objects."""
    if isinstance(value, str):
        try:
            return date.fromisoformat(value) if len(value) == 10 else value
        except ValueError:
            return value
    if isinstance(value, dict):
        return {k: str_to_dates(v) for k, v in value.items()}
    if isinstance(value, list):
        return [str_to_dates(v) for v in value]
    return value


def default_date(value):
    """The 'default' hook for json: called for objects json does not know."""
    if isinstance(value, date):
        return value.isoformat()
    raise TypeError(f"can not serialize {type(value).__name__}")


def build_data() -> dict:
    """Personal data: the period of my expenses as date objects."""
    try:
        records = json.loads(EXPENSES.read_text(encoding="utf-8"))
    except OSError:
        sys.exit("error: data/expenses.json not found, run task1.py first")
    days = [date.fromisoformat(r["date"]) for r in records]
    return {
        "owner": f"{NAME} {SURNAME}",
        "group": GROUP,
        "period": {"start": min(days), "end": max(days)},
        "expense_days": sorted(set(days)),
    }


def main() -> None:
    print(f"{NAME} {SURNAME}, {GROUP}")
    data = build_data()

    try:
        json.dumps(data)
    except TypeError as e:
        print(f"TypeError: {e}")

    # Спосіб 1: параметр default= (запис) + перетворення рядків назад (читання)
    text1 = json.dumps(data, default=default_date, ensure_ascii=False, indent=2)
    back1 = str_to_dates(json.loads(text1))
    print("method 1 (default=): equal =", back1 == data,
          "| start is date:", isinstance(back1["period"]["start"], date))

    # Спосіб 2: власні функції до запису і після читання
    text2 = json.dumps(dates_to_str(data), ensure_ascii=False, indent=2)
    back2 = str_to_dates(json.loads(text2))
    print("method 2 (own functions): equal =", back2 == data,
          "| start is date:", isinstance(back2["period"]["start"], date))

    (BASE / "dates.json").write_text(text2, encoding="utf-8")
    print("saved: dates.json")


if __name__ == "__main__":
    main()
