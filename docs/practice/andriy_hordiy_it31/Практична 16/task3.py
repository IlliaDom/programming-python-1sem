import json
from pathlib import Path
import sys

settings_path = Path(__file__).resolve().parent /"data" /"settings.json"
if not settings_path.exists():
    with open(settings_path, "w") as f:
        json.dump({
            "owner": "Andriy Hordiy",
            "group": "IT-31",
            "currency": "UAH",
            "monthly_limit": 6000,
            "categories": ["food", "transport", "fun"]
        }, f, indent=4)
        print("Settings file created")
elif settings_path.exists():
    with open(settings_path, "r") as f2:
        try:
            setings_reader = json.load(f2)
            print(setings_reader)
        except json.JSONDecodeError as error:
            print(f"error: invalid JSON at line {error.lineno}, column {error.colno}: {error.msg}", file=sys.stderr)
            sys.exit(1)
    my_expenses = 4300
    monthly_limit = setings_reader["monthly_limit"]
    print(f"limit: {monthly_limit}UAH, spent: {my_expenses}UAH, left: {monthly_limit - my_expenses}UAH")