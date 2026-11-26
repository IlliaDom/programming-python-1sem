from decimal import Decimal, ROUND_HALF_UP


class Money:
    def __init__(self, amount, currency="UAH"):
        value = Decimal(str(amount))
        self.cents = int((value * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
        self.currency = currency

    def _check_currency(self, other):
        if self.currency != other.currency:
            raise ValueError("Не можна виконувати операцію з різними валютами")

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._check_currency(other)
        result = Money(0, self.currency)
        result.cents = self.cents + other.cents
        return result

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._check_currency(other)
        result = Money(0, self.currency)
        result.cents = self.cents - other.cents
        return result

    def __mul__(self, number):
        if not isinstance(number, (int, float, Decimal)):
            return NotImplemented
        result = Money(0, self.currency)
        result.cents = int(
            (Decimal(self.cents) * Decimal(str(number))).quantize(
                Decimal("1"), rounding=ROUND_HALF_UP
            )
        )
        return result

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._check_currency(other)
        return self.cents == other.cents

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._check_currency(other)
        return self.cents < other.cents

    def __str__(self):
        return f"{self.cents / 100:.2f} {self.currency}"

    def __repr__(self):
        return f"Money({self.cents / 100:.2f}, {self.currency!r})"


if __name__ == "__main__":
    first = Money(0.1)
    second = Money(0.2)
    print("0.1 + 0.2 =", first + second)
    print("Точне порівняння:", first + second == Money(0.3))
    print("Float:", 0.1 + 0.2 == 0.3)
    try:
        print(Money(10, "UAH") + Money(5, "USD"))
    except ValueError as error:
        print("Помилка валюти:", error)
