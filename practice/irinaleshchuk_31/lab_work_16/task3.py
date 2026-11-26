import json
import sys

print("Лещук Ірина, IT-31")

settings_file = "settings.json"

default_settings = {
    "owner": "Лещук Ірина",
    "group": "IT-31",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "shopping", "entertainment"]
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
    print(f"JSON error in line {error.lineno}", file=sys.stderr)
    sys.exit(1)

with open("data/expenses.json", "r", encoding="utf-8") as file:
    expenses = json.load(file)

spent = sum(item["amount"] for item in expenses)
limit = settings["monthly_limit"]
left = limit - spent

print(f"limit: {limit:.2f} {settings['currency']}, spent: {spent:.2f} {settings['currency']}, left: {left:.2f} {settings['currency']}")