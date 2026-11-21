# --- ВАШІ ДАНІ: замініть на справжні ---
NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"


class Money:
    """Гроші: сума зберігається в копійках (int), без помилок округлення."""

    def __init__(self, amount, currency="UAH"):
        self.cents = round(amount * 100)
        self.currency = currency

    def _check(self, other):
        if self.currency != other.currency:
            raise ValueError(
                f"different currencies: {self.currency} and {other.currency}")

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._check(other)
        return Money((self.cents + other.cents) / 100, self.currency)

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._check(other)
        return Money((self.cents - other.cents) / 100, self.currency)

    def __mul__(self, factor):
        if isinstance(factor, bool) or not isinstance(factor, (int, float)):
            return NotImplemented
        return Money(self.cents * factor / 100, self.currency)

    __rmul__ = __mul__          # 3 * Money(10) теж працює

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.cents == other.cents and self.currency == other.currency

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._check(other)
        return self.cents < other.cents

    def __hash__(self):
        return hash((self.cents, self.currency))

    def __str__(self):
        return f"{self.cents / 100:.2f} {self.currency}"

    def __repr__(self):
        return f"Money({self.cents / 100}, {self.currency!r})"


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    print("float: 0.1 + 0.2 == 0.3 ->", 0.1 + 0.2 == 0.3)
    print("Money: Money(0.1) + Money(0.2) == Money(0.3) ->",
          Money(0.1) + Money(0.2) == Money(0.3))
    print("sum:   ", Money(0.1) + Money(0.2))
    print("sub:   ", Money(100) - Money(33.33))
    print("mul:   ", Money(85.5) * 3, "|", 2 * Money(10))
    print("repr:  ", repr(Money(12.3)))
    print("lt:    ", Money(5) < Money(10), "| eq:", Money(5) == Money(5.0))

    try:
        Money(10, "UAH") + Money(10, "USD")
    except ValueError as e:
        print("ValueError:", e)


if __name__ == "__main__":
    main()
