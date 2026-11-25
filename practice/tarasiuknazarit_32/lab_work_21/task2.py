"""
Завдання 2. Статичні методи-перевірки.
is_valid_date() і is_valid_amount() можна викликати без створення
обʼєкта; from_csv_line() використовує їх і пропускає некоректні рядки.
"""
from expense import Expense

# рядки з навмисно некоректними даними для перевірки пропуску
SAMPLE_LINES = [
    "2026-09-21;food;85.50;lunch",          # ок
    "2026-02-30;food;50.00;bad date",       # некоректна дата (30 лютого)
    "2026-10-01;transport;-20.00;negative", # від'ємна сума
    "2026-10-05;utilities;299.50;electricity",  # ок
]


def main() -> None:
    # Статичні методи викликаються прямо через клас, без жодного обʼєкта
    print("Expense.is_valid_date('2026-02-30'):", Expense.is_valid_date("2026-02-30"))
    print("Expense.is_valid_date('2026-09-21'):", Expense.is_valid_date("2026-09-21"))
    print("Expense.is_valid_amount('-20'):", Expense.is_valid_amount("-20"))
    print("Expense.is_valid_amount('85.50'):", Expense.is_valid_amount("85.50"))

    print("\nзавантаження рядків з перевіркою:")
    loaded = [Expense.from_csv_line(line) for line in SAMPLE_LINES]
    loaded = [e for e in loaded if e is not None]

    print(f"\nуспішно завантажено: {len(loaded)} з {len(SAMPLE_LINES)}")
    for expense in loaded:
        print(" -", expense.describe())


if __name__ == "__main__":
    main()
