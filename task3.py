
from task1 import Money


class ExpenseBook:
    def __init__(self, expenses=None):
        self.expenses = list(expenses) if expenses else []

    def __len__(self):
        return len(self.expenses)

    def __contains__(self, category):
        return any(
            expense[1] == category
            for expense in self.expenses
        )

    def __iter__(self):
        return iter(self.expenses)

    def __getitem__(self, index):
        return self.expenses[index]

    def __add__(self, other):
        if not isinstance(other, ExpenseBook):
            return NotImplemented

        return ExpenseBook(self.expenses + other.expenses)

    def total(self):
        return sum(
            (expense[2] for expense in self.expenses),
            Money(0)
        )

    def __gt__(self, budget):
        if not isinstance(budget, Money):
            return NotImplemented

        return self.total() > budget

    def __str__(self):
        return (
            f"Книга витрат: {len(self)} записів, "
            f"загальна сума: {self.total()}"
        )


def load_expenses(filename):
    expenses = []

    with open(filename, "r", encoding="utf-8-sig") as file:
        for line in file:
            if not line.strip():
                continue

            parts = line.strip().split(";")

            if parts[0].lower() in ("date", "дата"):
                continue

            if len(parts) < 3:
                continue

            try:
                date = parts[0]
                category = parts[1]
                amount = float(parts[2].replace(",", "."))

                expenses.append((date, category, Money(amount)))

            except ValueError:
                print("Рядок пропущено:", line.strip())

    return expenses


if __name__ == "__main__":
    expenses = load_expenses("data/expenses.csv")

    first_half = ExpenseBook([
        expense for expense in expenses
        if int(expense[0].split("-")[2]) <= 15
    ])

    second_half = ExpenseBook([
        expense for expense in expenses
        if int(expense[0].split("-")[2]) > 15
    ])

    # Об'єднання двох книг
    month = first_half + second_half

    print("Перша половина місяця:")
    print(first_half)

    print("\nДруга половина місяця:")
    print(second_half)

    print("\nОб'єднана книга:")
    print(month)

    print("\nКількість записів:")
    print("Перша половина:", len(first_half))
    print("Друга половина:", len(second_half))
    print("Разом:", len(month))

    print("\nПеревірка категорії:")
    print("'food' in month:", "food" in month)

    print("\nВитрати у циклі:")
    for expense in month:
        print(expense[0], expense[1], expense[2])

    print("\nПерший запис:")
    if len(month) > 0:
        print(month[0])
