from task1 import Money
from task3 import ExpenseBook, load_expenses


class BudgetBook(ExpenseBook):
    def __gt__(self, budget):
        if not isinstance(budget, Money):
            return NotImplemented
        return self.total() > budget

    def __lt__(self, budget):
        if not isinstance(budget, Money):
            return NotImplemented
        return self.total() < budget


book = BudgetBook(load_expenses("data/expenses.csv"))
budget = Money(3000)

print("budget:", budget)
print("spent:", book.total())
print("book > Money(1000):", book > Money(1000))
print("book > budget:", book > budget)

if book > budget:
    print("over budget by", book.total() - budget)
else:
    print("within budget, left", budget - book.total())
