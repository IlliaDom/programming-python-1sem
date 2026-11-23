import json
import os
import sys

print("Vlad Kudryk, IT-32")

default = {
    "owner": "Vlad Kudryk",
    "group": "IT-32",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"],
}

if not os.path.exists("settings.json"):
    with open("settings.json", "w", encoding="utf-8") as f:
        json.dump(default, f, indent=2, ensure_ascii=False)
    print("settings.json not found, default created")
else:
    try:
        with open("settings.json", encoding="utf-8") as f:
            settings = json.load(f)
    except json.JSONDecodeError as e:
        print("JSON error, line:", e.lineno, file=sys.stderr)
        sys.exit(1)

    with open("data/expenses.json", encoding="utf-8") as f:
        expenses = json.load(f)

    spent = sum(r["amount"] for r in expenses)
    limit = settings["monthly_limit"]
    cur = settings["currency"]
    left = limit - spent
    print(f"limit: {limit:.2f} {cur}, spent: {spent:.2f} {cur}, left: {left:.2f} {cur}")