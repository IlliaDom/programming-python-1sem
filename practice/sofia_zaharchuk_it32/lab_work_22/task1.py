"""Practice 22, task 1: class Money with overloaded operators."""
from collections import namedtuple
from datetime import date
from functools import total_ordering

NAME = "Sofiia Zakharchuk"
GROUP = "IT-32"
CSV_PATH = "data/expenses.csv"


@total_ordering
class Money:
    """An immutable amount of money stored in cents (int)."""

    def __init__(self, amount=0, currency="UAH"):
        self._cents = round(amount * 100)
        self._currency = currency

    @property
    def cents(self):
        return self._cents

    @property
    def currency(self):
        return self._currency

    def _same_currency(self, other):
        if self._currency != other._currency:
            raise ValueError(f"different currencies: {self._currency} and {other._currency}")

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented  # Python will try other.__radd__, then raise TypeError
        self._same_currency(other)
        return Money((self._cents + other._cents) / 100, self._currency)

    def __radd__(self, other):
        # sum() starts from the int 0, so 0 + Money must work
        return self if other == 0 else NotImplemented

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._same_currency(other)
        return Money((self._cents - other._cents) / 100, self._currency)

    def __mul__(self, factor):
        if not isinstance(factor, (int, float)):
            return NotImplemented
        return Money(self._cents * factor / 100, self._currency)

    __rmul__ = __mul__

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return (self._cents, self._currency) == (other._cents, other._currency)

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._same_currency(other)
        return self._cents < other._cents

    def __hash__(self):
        return hash((self._cents, self._currency))

    def __str__(self):
        return f"{self._cents / 100:.2f} {self._currency}"

    def __repr__(self):
        return f"Money({self._cents / 100}, {self._currency!r})"


Expense = namedtuple("Expense", "date category money comment")


def load_expenses(path, currency="UAH"):
    """Read expenses.csv (date, category, amount[, comment]); bad rows are skipped."""
    expenses = []
    with open(path, encoding="utf-8-sig") as file:
        for number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            if number == 1 and not line.strip()[0].isdigit():
                continue  # header row
            sep = ";" if ";" in line else ","
            parts = [p.strip() for p in line.strip().split(sep, 3)]
            try:
                day = date.fromisoformat(parts[0])
                amount = float(parts[2])
                comment = parts[3] if len(parts) > 3 else ""
                expenses.append(Expense(day, parts[1], Money(amount, currency), comment))
            except (ValueError, IndexError) as error:
                print(f"skip line {number}: {error}")
    return expenses


if __name__ == "__main__":
    print(f"{NAME}, {GROUP}")
    print("float:", 0.1 + 0.2 == 0.3)
    print("Money:", Money(0.1) + Money(0.2) == Money(0.3))
    print(Money(0.1) + Money(0.2))
    print(Money(100) - Money(85.5))
    print(Money(42.3) * 3, "|", 3 * Money(42.3))
    print(repr(Money(85.5)))
    print(Money(30) < Money(85.5), Money(30) == Money(30.0), Money(30) >= Money(85.5))
    try:
        Money(10) + Money(10, "USD")
    except ValueError as error:
        print("error:", error)
