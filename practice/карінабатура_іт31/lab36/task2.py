import json
from datetime import date
from pathlib import Path

STUDENT_INFO = "Batura Karina, IT-31"
INPUT_PATH = Path("data/expenses.json")
OUTPUT_PATH = Path("data/expenses_updated.json")


def main() -> None:
    print(STUDENT_INFO)

    with INPUT_PATH.open("r", encoding="utf-8") as file:
        expenses = json.load(file)

    # 1. Додаємо новий запис з сьогоднішньою датою
    new_record = {
        "date": date.today().isoformat(),
        "category": "food",
        "amount": 145.50,
        "comment": "Обід у їдальні",
    }
    expenses.append(new_record)
    added_count = 1

    # 2. Видаляємо записи з сумою менше 10
    filtered_expenses = [item for item in expenses if item["amount"] >= 10]
    removed_count = len(expenses) - len(filtered_expenses)

    # 3. Записуємо у новий файл
    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        json.dump(filtered_expenses, file, indent=2, ensure_ascii=False)

    print(f"added: {added_count}, removed: {removed_count}")
    print(f"saved: {OUTPUT_PATH.as_posix()} (total records: {len(filtered_expenses)})")


if __name__ == "__main__":
    main()