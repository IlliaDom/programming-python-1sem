"""
Клас Money: сума зберігається в копійках (int), щоб уникнути помилок
округлення float. Перевантажені оператори: +, -, *, ==, <, str(), repr().
"""


class Money:
    def __init__(self, amount: float, currency: str = "UAH"):
        self.cents = round(amount * 100)
        self.currency = currency

    def _check_same_currency(self, other: "Money") -> None:
        if self.currency != other.currency:
            raise ValueError("different currencies")

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._check_same_currency(other)
        return Money((self.cents + other.cents) / 100, self.currency)

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._check_same_currency(other)
        return Money((self.cents - other.cents) / 100, self.currency)

    def __mul__(self, factor):
        if not isinstance(factor, (int, float)):
            return NotImplemented
        return Money((self.cents * factor) / 100, self.currency)

    __rmul__ = __mul__  # щоб працювало й 2 * Money(10)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.cents == other.cents and self.currency == other.currency

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._check_same_currency(other)
        return self.cents < other.cents

    def __str__(self) -> str:
        return f"{self.cents / 100:.2f} {self.currency}"

    def __repr__(self) -> str:
        return f"Money({self.cents / 100!r}, {self.currency!r})"
