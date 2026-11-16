import json
import sys

print("Nikita Krilovets, IT-31")

settings_file = "settings.json"

default_settings = {
    "owner": "Nikita Krilovets",
    "group": "IT-31",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"]
}

try:
    with open(settings_file, "r", encoding="utf-8") as file:
        settings = json.load(file)

except FileNotFoundError:
    with open(settings_file, "w", encoding="utf-8") as file:
        json.dump(default_settings, file, indent=2, ensure_ascii=False)

    print("settings.json not found, default created")
    sys.exit(0)

except json.JSONDecodeError as error:
    print(f"JSON error at line {error.lineno}", file=sys.stderr)
    sys.exit(1)

with open("data/expenses.json", "r", encoding="utf-8") as file:
    records = json.load(file)

spent = sum(record["amount"] for record in records)

limit = settings["monthly_limit"]
left = limit - spent

print(f"limit: {limit:.2f} {settings['currency']}, spent: {spent:.2f} {settings['currency']}, left: {left:.2f} {settings['currency']}")
