import sys

from task1 import CSV_FILE, GROUP, NAME, SURNAME, Expense, load_csv


class Income:
    def __init__(self, source, amount):
        self.source = source
        self.amount = amount

    def balance_change(self):
        return self.amount


class Transfer:
    """Переказ між своїми картками: баланс не змінюється."""
    def __init__(self, from_card, to_card, amount):
        self.from_card = from_card
        self.to_card = to_card
        self.amount = amount

    def balance_change(self):
        return 0.0


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    if not CSV_FILE.is_file():
        print(f"error: {CSV_FILE} not found", file=sys.stderr)
        sys.exit(1)

    items = load_csv(CSV_FILE) + [
        Income("scholarship", 2000.00),
        Income("part-time job", 600.00),
        Transfer("card A", "card B", 500.00),
    ]

    income = expenses = transfers = 0.0
    for item in items:                    
        change = item.balance_change()
        if change > 0:
            income += change
        elif change < 0:
            expenses += change
        else:
            transfers += change

    print(f"income:    {income:>9.2f}")
    print(f"expenses:  {expenses:>9.2f}")
    print(f"transfers: {transfers:>9.2f}")
    print(f"balance:   {income + expenses + transfers:>9.2f}")


if __name__ == "__main__":
    main()
