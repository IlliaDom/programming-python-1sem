import json
import sys
from pathlib import Path

print("Maria Vovk, І-23")

BASE_DIR = Path(__file__).parent
settings_path = BASE_DIR / "settings.json"
expenses_path = BASE_DIR / "data" / "expenses.csv"

default_settings = {
    "owner": "Maria Vovk",
    "group": "І-23",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"]
}

if not settings_path.exists():
    with settings_path.open("w", encoding="utf-8") as file:
        json.dump(default_settings, file, indent=2, ensure_ascii=False)
    print("settings.json not found, default created")
    sys.exit(0)

try:
    with settings_path.open("r", encoding="utf-8") as file:
        settings = json.load(file)
except json.JSONDecodeError as error:
    print(f"Invalid JSON in settings.json at line {error.lineno}", file=sys.stderr)
    sys.exit(1)

total = 0.0
import csv
with expenses_path.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        total += float(row["amount"])

limit = float(settings["monthly_limit"])
left = limit - total
print(f"owner: {settings['owner']}")
print(f"group: {settings['group']}")
print(f"currency: {settings['currency']}")
print(f"categories: {', '.join(settings['categories'])}")
print(f"limit: {limit:.2f} {settings['currency']}, spent: {total:.2f} {settings['currency']}, left: {left:.2f} {settings['currency']}")
