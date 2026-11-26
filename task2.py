
from task1 import Expense

print("Перевірка дат:")
print("2026-02-28:", Expense.is_valid_date("2026-02-28"))
print("2026-02-30:", Expense.is_valid_date("2026-02-30"))
print("28-02-2026:", Expense.is_valid_date("28-02-2026"))

print("\nПеревірка сум:")
print("85.50:", Expense.is_valid_amount("85.50"))
print("-3:", Expense.is_valid_amount("-3"))
print("abc:", Expense.is_valid_amount("abc"))
