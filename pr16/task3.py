import json
import sys
from pathlib import Path

NAME = "Nazar Mischuk IT-32"

BASE = Path(__file__).parent
SETTINGS_PATH = BASE / "settings.json"
CSV_PATH = BASE / "data" / "expenses.csv"

DEFAULT_SETTINGS = {
    "owner": "Ivan Petrenko",
    "group": "PZ-11",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "study", "entertainment"],
}


def total_spent(path):
    total = 0.0
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            total += float(line.split(";")[2])
    return total


def main():
    print(NAME)

    if not SETTINGS_PATH.exists():
        with open(SETTINGS_PATH, "w", encoding="utf-8") as file:
            json.dump(DEFAULT_SETTINGS, file, indent=2, ensure_ascii=False)
        print("settings.json not found, default created")
        return

    try:
        with open(SETTINGS_PATH, encoding="utf-8") as file:
            settings = json.load(file)
    except json.JSONDecodeError as error:
        print(f"settings.json is broken at line {error.lineno}: {error.msg}", file=sys.stderr)
        sys.exit(1)

    limit = settings["monthly_limit"]
    currency = settings["currency"]
    spent = total_spent(CSV_PATH)
    left = limit - spent
    print(f"owner: {settings['owner']}, group: {settings['group']}")
    print(f"categories: {', '.join(settings['categories'])}")
    print(f"limit: {limit:.2f} {currency}, spent: {spent:.2f} {currency}, left: {left:.2f} {currency}")
    if left < 0:
        print("WARNING: limit exceeded!")


if __name__ == "__main__":
    main()
