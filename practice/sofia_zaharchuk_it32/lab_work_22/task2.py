"""Practice 22, task 2: sorting, sum() and NotImplemented."""
from task1 import CSV_PATH, GROUP, NAME, Money, load_expenses


class NaiveMoney:
    """A version of __add__ without NotImplemented, for comparison."""

    def __init__(self, cents):
        self.cents = cents

    def __add__(self, other):
        return NaiveMoney(self.cents + other.cents)


if __name__ == "__main__":
    print(f"{NAME}, {GROUP}")
    expenses = load_expenses(CSV_PATH)
    items = [e.money for e in expenses]
    print("count:", len(items))

    print("--- sorted (works thanks to __lt__) ---")
    ordered = sorted(items)
    print("smallest 3:", ", ".join(map(str, ordered[:3])))
    print("biggest 3: ", ", ".join(map(str, ordered[-3:])))
    print("min:", min(items), "| max:", max(items))

    print("--- sum ---")
    total = sum(items, Money(0))
    print("sum(items, Money(0)):", total)
    print("sum(items):          ", sum(items))
    print("sum([], Money(0)):   ", sum([], Money(0)))
    print("float sum of csv:    ", round(sum(i.cents for i in items) / 100, 2))
    print("matches:", total.cents == sum(i.cents for i in items))

    print("--- Money(10) + 5 ---")
    try:
        NaiveMoney(10) + 5
    except Exception as error:
        print("without NotImplemented:", type(error).__name__, "-", error)
    try:
        Money(10) + 5
    except TypeError as error:
        print("with NotImplemented:   ", type(error).__name__, "-", error)
