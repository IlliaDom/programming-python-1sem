import json
import sys
from pathlib import Path

print("Vlad Mushka, IT31")

settings_path = Path("settings.json")
expenses_path = Path("data/expenses.json")

default_settings = {
    "owner": "Vlad Mushka",
    "group": "IT31",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"]
}

if not settings_path.exists():
    with open(settings_path, "w", encoding="utf-8") as file:
        json.dump(default_settings, file, indent=2, ensure_ascii=False)

    print("settings.json not found, default created")
else:
    try:
        with open(settings_path, "r", encoding="utf-8") as file:
            settings = json.load(file)

    except json.JSONDecodeError as error:
        print(f"JSON error on line {error.lineno}", file=sys.stderr)
        sys.exit(1)

    with open(expenses_path, "r", encoding="utf-8") as file:
        expenses = json.load(file)

    spent = sum(record["amount"] for record in expenses)
    limit = settings["monthly_limit"]
    left = limit - spent

    print(f"limit: {limit:.2f} {settings['currency']}, "
          f"spent: {spent:.2f} {settings['currency']}, "
          f"left: {left:.2f} {settings['currency']}")