import json
import sys
from pathlib import Path

NAME, SURNAME, GROUP = "Sofiia", "Zakharchuk", "IT-32"

BASE = Path(__file__).resolve().parent
SETTINGS = BASE / "settings.json"
EXPENSES = BASE / "data" / "expenses.json"

DEFAULTS = {
    "owner": f"{NAME} {SURNAME}",
    "group": GROUP,
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["coffee", "food", "transport", "snacks", "stationery"],
}


def load_settings() -> dict | None:
    """Return settings, or None if the file was just created."""
    if not SETTINGS.exists():
        SETTINGS.write_text(json.dumps(DEFAULTS, indent=2, ensure_ascii=False), encoding="utf-8")
        print("settings.json not found, default created")
        return None
    try:
        user = json.loads(SETTINGS.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        # Файл не перезаписуємо: лише повідомляємо про помилку
        print(f"error: settings.json is broken at line {e.lineno}, column {e.colno}: {e.msg}", file=sys.stderr)
        sys.exit(1)
    return {**DEFAULTS, **user}


def total_spent() -> float:
    try:
        records = json.loads(EXPENSES.read_text(encoding="utf-8"))
    except OSError:
        sys.exit("error: data/expenses.json not found, run task1.py first")
    return sum(r["amount"] for r in records)


def main() -> None:
    print(f"{NAME} {SURNAME}, {GROUP}")
    settings = load_settings()
    if settings is None:
        return
    for key, value in settings.items():
        print(f"{key}: {value}")
    spent = total_spent()
    limit = settings["monthly_limit"]
    cur = settings["currency"]
    print(f"limit: {limit:.2f} {cur}, spent: {spent:.2f} {cur}, left: {limit - spent:.2f} {cur}")


if __name__ == "__main__":
    main()
