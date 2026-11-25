"""
Завдання 3. Колекція витрат.
Ділимо витрати на дві книги за датою (1-15 і 16-31) і обʼєднуємо
їх оператором +.
"""
from expense_book import ExpenseBook

EXPENSES_FILE = "data/expenses.csv"


def main() -> None:
    book = ExpenseBook.from_csv(EXPENSES_FILE)

    first_half = ExpenseBook([e for e in book if int(e.date.split("-")[2]) <= 15])
    second_half = ExpenseBook([e for e in book if int(e.date.split("-")[2]) > 15])

    print("перша половина місяця:", first_half)
    print("друга половина місяця:", second_half)

    merged = first_half + second_half
    print("\nобʼєднана книга:", merged)
    print("len(merged) == len(first) + len(second):",
          len(merged) == len(first_half) + len(second_half))

    print("\n'food' in merged:", "food" in merged)
    print("'rent' in merged:", "rent" in merged)

    print("\nmerged[0]:", merged[0])

    print("\nусі витрати через for:")
    for expense in merged:
        print(" -", expense)


if __name__ == "__main__":
    main()
