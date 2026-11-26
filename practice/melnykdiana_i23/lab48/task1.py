"""Завдання 1. Грошова сума у цілих копійках."""

from decimal import Decimal, ROUND_HALF_UP


class Money:
    def __init__(self, amount, currency="UAH"):
        self.cents = int((Decimal(str(amount)) * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
        self.currency = currency.upper()

    @classmethod
    def from_cents(cls, cents, currency="UAH"):
        obj = cls(0, currency)
        obj.cents = int(cents)
        return obj

    def _check_currency(self, other):
        if self.currency != other.currency:
            raise ValueError("different currencies")

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._check_currency(other)
        return Money.from_cents(self.cents + other.cents, self.currency)

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._check_currency(other)
        return Money.from_cents(self.cents - other.cents, self.currency)

    def __mul__(self, number):
        if not isinstance(number, (int, float, Decimal)):
            return NotImplemented
        cents = int((Decimal(self.cents) * Decimal(str(number))).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
        return Money.from_cents(cents, self.currency)

    __rmul__ = __mul__

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.currency == other.currency and self.cents == other.cents

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._check_currency(other)
        return self.cents < other.cents

    def __str__(self):
        return f"{self.cents / 100:.2f} {self.currency}"

    def __repr__(self):
        return f"Money({self.cents / 100:.2f}, {self.currency!r})"


def main():
    print(f"Money(0.1) + Money(0.2) = {Money(0.1) + Money(0.2)}")
    print(f"Money(0.1) + Money(0.2) == Money(0.3): {Money(0.1) + Money(0.2) == Money(0.3)}")
    print(f"0.1 + 0.2 == 0.3 для float: {0.1 + 0.2 == 0.3}")
    print(f"Віднімання: {Money(10) - Money(3.25)}")
    print(f"Множення: {Money(12.5) * 3}")
    print(f"repr: {Money(12.5)!r}")
    try:
        print(Money(10, "UAH") + Money(5, "USD"))
    except ValueError as error:
        print(f"Помилка різних валют: {error}")


if __name__ == "__main__":
    main()
