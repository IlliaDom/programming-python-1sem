import csv
from pathlib import Path


class Expense:
    def __init__(self, date: str, category: str, amount: float):
        self.date = date
        self.category = category
        self.amount = float(amount)

    def monthly_cost(self) -> float:
        return self.amount


class RecurringExpense(Expense):
    def __init__(self, date: str, category: str, amount: float, times_per_month: int):
        super().__init__(date, category, amount)
        self.times_per_month = int(times_per_month)

    def monthly_cost(self) -> float:
        return self.amount * self.times_per_month


class SharedExpense(Expense):
    def __init__(self, date: str, category: str, amount: float, people: int):
        super().__init__(date, category, amount)
        if people <= 0:
            raise ValueError("Кількість людей має бути більшою за 0.")
        self.people = int(people)

    def monthly_cost(self) -> float:
        return self.amount / self.people


def load_csv_rows() -> list[dict[str, str]]:
    base_dir = Path(__file__).resolve().parent
    for candidate in [
        base_dir / "data" / "expenses.csv",
        Path("lab44/data/expenses.csv"),
        Path("data/expenses.csv"),
    ]:
        if candidate.exists():
            with candidate.open(mode="r", encoding="utf-8", newline="") as f:
                return list(csv.DictReader(f))
    return []


def build_expenses() -> list[Expense]:
    rows = load_csv_rows()
    food_amount = float(rows[0]["amount_uah"]) if len(rows) > 0 else 450.00
    transport_amount = float(rows[1]["amount_uah"]) if len(rows) > 1 else 180.00
    cafe_amount = float(rows[2]["amount_uah"]) if len(rows) > 2 else 220.00
    books_amount = float(rows[3]["amount_uah"]) if len(rows) > 3 else 398.00

    return [
        # Звичайні витрати з data/expenses.csv
        Expense("2026-11-02", rows[0]["category"] if len(rows) > 0 else "Їжа", food_amount),
        Expense("2026-11-05", rows[3]["category"] if len(rows) > 3 else "Книги та канцелярія", books_amount),
        # Регулярні витрати (щонайменше дві)
        RecurringExpense("2026-11-01", rows[1]["category"] if len(rows) > 1 else "Транспорт", transport_amount, 4),
        RecurringExpense("2026-11-03", rows[2]["category"] if len(rows) > 2 else "Кав'ярня", cafe_amount, 3),
        # Спільні витрати (щонайменше дві)
        SharedExpense("2026-11-04", "Оренда житла", 12000.00, 2),
        SharedExpense("2026-11-06", "Інтернет та комунальні", 2400.00, 3),
    ]


def total_monthly_cost(expenses: list[Expense]) -> float:
    total = 0.0
    for item in expenses:
        total += item.monthly_cost()
    return total


if __name__ == "__main__":
    expenses = build_expenses()
    for exp in expenses:
        print(f"{exp.date} | {exp.category:<22} | місячна вартість: {exp.monthly_cost():.2f} грн")

    print(f"\nЗагальна місячна вартість: {total_monthly_cost(expenses):.2f} грн")