
from functools import total_ordering


@total_ordering
class Money:
    def __init__(self, amount, currency="UAH"):
        self.cents = round(amount * 100)
        self.currency = currency

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented

        if self.currency != other.currency:
            raise ValueError("Різні валюти")

        return Money(
            (self.cents + other.cents) / 100,
            self.currency
        )

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented

        if self.currency != other.currency:
            raise ValueError("Різні валюти")

        return Money(
            (self.cents - other.cents) / 100,
            self.currency
        )

    def __mul__(self, number):
        if not isinstance(number, (int, float)):
            return NotImplemented

        return Money(
            round(self.cents * number) / 100,
            self.currency
        )

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented

        return (
            self.cents == other.cents
            and self.currency == other.currency
        )

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented

        if self.currency != other.currency:
            raise ValueError("Не можна порівнювати різні валюти")

        return self.cents < other.cents

    def __str__(self):
        return f"{self.cents / 100:.2f} {self.currency}"

    def __repr__(self):
        return f"Money({self.cents / 100}, {self.currency!r})"


if __name__ == "__main__":
    a = Money(0.1)
    b = Money(0.2)

    print("Додавання:", a + b)
    print("Порівняння:", a + b == Money(0.3))
    print("Віднімання:", Money(100) - Money(85.5))
    print("Множення:", Money(42.3) * 3)

    print("Рядкове представлення:", str(a))
    print("Представлення для програміста:", repr(a))

    print("Float:", 0.1 + 0.2 == 0.3)

    try:
        print(Money(10) + Money(10, "USD"))
    except ValueError as error:
        print("Помилка:", error)

    try:
        print(Money(10) + 5)
    except TypeError as error:
        print("Помилка:", error)
