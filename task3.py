import json, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
SETTINGS = BASE / "settings.json"
EXPENSES = BASE / "data/expenses.json"
print("Anatolii Kurotych, PZ-11")

defaults = {
    "owner": "Anatolii Kurotych",
    "group": "PZ-11",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun", "coffee", "books", "internet"]
}

if not SETTINGS.exists():
    with SETTINGS.open("w", encoding="utf-8") as file:
        json.dump(defaults, file, indent=2, ensure_ascii=False)
    print("settings.json not found, default created")
    raise SystemExit(0)

try:
    with SETTINGS.open(encoding="utf-8") as file:
        settings = json.load(file)
except json.JSONDecodeError as error:
    print(f"JSON error at line {error.lineno}: {error.msg}", file=sys.stderr)
    raise SystemExit(1)

print(json.dumps(settings, indent=2, ensure_ascii=False))
with EXPENSES.open(encoding="utf-8") as file:
    expenses = json.load(file)

spent = sum(float(item["amount"]) for item in expenses)
limit = float(settings["monthly_limit"])
print(f"limit: {limit:.2f} {settings['currency']}, spent: {spent:.2f} {settings['currency']}, left: {limit-spent:.2f} {settings['currency']}")
