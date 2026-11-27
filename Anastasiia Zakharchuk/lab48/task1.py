class Money:
    def __init__(self, amount, currency="UAH"):
        self.cents = round(amount * 100)
        self.currency = currency

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("different currencies")
        return Money((self.cents + other.cents) / 100, self.currency)

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("different currencies")
        return Money((self.cents - other.cents) / 100, self.currency)

    def __mul__(self, number):
        if not isinstance(number, (int, float)):
            return NotImplemented
        return Money(self.cents * number / 100, self.currency)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.cents == other.cents and self.currency == other.currency

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("different currencies")
        return self.cents < other.cents

    def __str__(self):
        return f"{self.cents / 100:.2f} {self.currency}"

    def __repr__(self):
        return f"Money({self.cents / 100}, '{self.currency}')"


if __name__ == "__main__":
    print(Money(0.1) + Money(0.2))
    print(0.1 + 0.2 == 0.3)
    print(Money(0.1) + Money(0.2) == Money(0.3))

    print(Money(100) - Money(30.5))
    print(Money(25.5) * 3)
    print(repr(Money(5)))
    print(Money(5) < Money(10))

    try:
        Money(10, "UAH") + Money(10, "USD")
    except ValueError as error:
        print("ValueError:", error)
