import json
import sys
from pathlib import Path

print("Karina Pikul, IT-32")

BASE_DIR = Path(__file__).parent
SETTINGS_FILE = BASE_DIR / "settings.json"
EXPENSES_FILE = BASE_DIR / "data" / "expenses.json"

DEFAULT_SETTINGS = {
    "owner": "Karina Pikul",
    "group": "IT-32",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"]
}

if not SETTINGS_FILE.exists():
    with open(SETTINGS_FILE, "w", encoding="utf-8") as file:
        json.dump(DEFAULT_SETTINGS, file, indent=2, ensure_ascii=False)

    print("Файл settings.json не знайдено. Створено налаштування за замовчуванням.")

else:
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as file:
            settings = json.load(file)

        print("Налаштування програми:")
        print(json.dumps(settings, indent=2, ensure_ascii=False))

        with open(EXPENSES_FILE, "r", encoding="utf-8") as file:
            expenses = json.load(file)

        total_spent = sum(expense["amount"] for expense in expenses)
        monthly_limit = settings["monthly_limit"]
        remaining = monthly_limit - total_spent

        print(f"Ліміт: {monthly_limit:.2f} {settings['currency']}")
        print(f"Витрачено: {total_spent:.2f} {settings['currency']}")
        print(f"Залишилося: {remaining:.2f} {settings['currency']}")

    except json.JSONDecodeError as error:
        print(
            f"Помилка JSON у рядку {error.lineno}: {error.msg}",
            file=sys.stderr
        )
        sys.exit(1)
