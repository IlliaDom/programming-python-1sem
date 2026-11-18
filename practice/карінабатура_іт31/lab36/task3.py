import json
import sys
from pathlib import Path

STUDENT_INFO = "Batura Karina, IT-31"
SETTINGS_PATH = Path("settings.json")
EXPENSES_PATH = Path("data/expenses.json")

DEFAULTS = {
    "owner": "Batura Karina",
    "group": "IT-31",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"],
}


def main() -> None:
    print(STUDENT_INFO)

    # 1. Якщо файлу немає — створюємо зі значеннями за замовчуванням
    if not SETTINGS_PATH.exists():
        SETTINGS_PATH.write_text(
            json.dumps(DEFAULTS, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        print("settings.json not found, default created")
        return

    # 2. Якщо файл є — читаємо та обробляємо можливе пошкодження JSON
    try:
        raw_text = SETTINGS_PATH.read_text(encoding="utf-8")
        user_settings = json.loads(raw_text)
    except json.JSONDecodeError as error:
        print(
            f"error: invalid JSON in {SETTINGS_PATH.name} at line {error.lineno}",
            file=sys.stderr,
        )
        sys.exit(1)

    settings = {**DEFAULTS, **user_settings}

    # Читаємо витрати для підрахунку загальної суми
    with EXPENSES_PATH.open("r", encoding="utf-8") as file:
        expenses = json.load(file)

    total_spent = sum(item["amount"] for item in expenses)
    limit = float(settings["monthly_limit"])
    left = limit - total_spent
    currency = settings["currency"]

    print(f"limit: {limit:.2f} {currency}, spent: {total_spent:.2f} {currency}, left: {left:.2f} {currency}")


if __name__ == "__main__":
    main()