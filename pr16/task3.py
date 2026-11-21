import json
import sys
from pathlib import Path

NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"

BASE = Path(__file__).resolve().parent
SETTINGS = BASE / "settings.json"
EXPENSES = BASE / "data" / "expenses.json"

DEFAULTS = {
    "owner": f"{NAME} {SURNAME}",
    "group": GROUP,
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"],
}


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    if not SETTINGS.exists():
        with SETTINGS.open("w", encoding="utf-8") as f:
            json.dump(DEFAULTS, f, indent=2, ensure_ascii=False)
        print("settings.json not found, default created")
        return

    try:
        with SETTINGS.open(encoding="utf-8") as f:
            settings = json.load(f)
    except json.JSONDecodeError as e:
        print(f"error: settings.json is broken at line {e.lineno}: {e.msg}",
              file=sys.stderr)
        sys.exit(1)

    if not EXPENSES.is_file():
        print(f"error: {EXPENSES} not found, run task1.py first",
              file=sys.stderr)
        sys.exit(1)
    with EXPENSES.open(encoding="utf-8") as f:
        spent = sum(r["amount"] for r in json.load(f))

    limit = settings["monthly_limit"]
    cur = settings["currency"]
    print(f"limit: {limit:.2f} {cur}, spent: {spent:.2f} {cur}, "
          f"left: {limit - spent:.2f} {cur}")


if __name__ == "__main__":
    main()
