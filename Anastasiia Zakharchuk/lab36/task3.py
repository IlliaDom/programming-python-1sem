import json
import os
import sys

print("Anastasia Zakharchuk, IT-32")

SETTINGS_FILE = "settings.json"

default_settings = {
    "owner": "Anastasia Zakharcuk",
    "group": "IT-32",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"],
}

if not os.path.exists(SETTINGS_FILE):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(default_settings, f, indent=2, ensure_ascii=False)
    print("settings.json not found, default created")
else:
    try:
        with open(SETTINGS_FILE, encoding="utf-8") as f:
            settings = json.load(f)
    except json.JSONDecodeError as e:
        print(f"settings.json is broken, error on line {e.lineno}: {e.msg}", file=sys.stderr)
        sys.exit(1)

    with open("data/expenses.json", encoding="utf-8") as f:
        records = json.load(f)

    spent = sum(r["amount"] for r in records)
    limit = settings["monthly_limit"]
    currency = settings["currency"]
    print(f"limit: {limit:.2f} {currency}, spent: {spent:.2f} {currency}, left: {limit - spent:.2f} {currency}")
