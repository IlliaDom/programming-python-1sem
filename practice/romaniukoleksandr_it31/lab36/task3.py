import json
import sys
from pathlib import Path

print("Oleksandr Romaniuk, IT-31")

SETTINGS = Path("settings.json")

DEFAULT = {
  "owner": "Oleksandr Romaniuk",
  "group": "IT-31",
  "currency": "UAH",
  "monthly_limit": 6000,
  "categories": ["food", "transport", "fun"]
}

#  = json.loads(settings_path)

def load_settings():
    if not SETTINGS.exists():
        SETTINGS.write_text(json.dumps(DEFAULT), encoding="utf-8")
        print("settings.json was created, because it didn't exist")
        return
    
    try:
        user_settings = json.loads(SETTINGS.read_text(encoding="utf-8"))
        expenses = 0

        with open("data/expenses.json", "r", encoding="utf-8") as f:
            standart_f = json.load(f)
            for line in standart_f:
                expenses += line["amount"]

        print(f"owner: {user_settings["owner"]}, monthly_limit: {user_settings["monthly_limit"]} {user_settings["currency"]}, spent: {expenses} {user_settings["currency"]}, left: {user_settings["monthly_limit"] - expenses} {user_settings["currency"]}")
    except json.JSONDecodeError as err:
        sys.stderr.write(f"error occured: line {err.lineno}, column {err.colno}: {err.msg}")
        sys.exit(1)

load_settings()