from task1 import Money
from task3 import ExpenseBook, load_expenses


if __name__ == "__main__":
    expenses = load_expenses()
    book = ExpenseBook(expenses)
    budget = Money(15000)
    remaining = budget - book.total

    print("Загальна сума витрат:", book.total)
    print("Місячний бюджет:", budget)
    print("Залишок бюджету:", remaining)
    print("Витрати перевищують бюджет:", book > budget)
    print("У межах бюджету:", not (book > budget))
