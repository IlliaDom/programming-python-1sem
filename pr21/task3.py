import sys

from task1 import CSV_FILE, GROUP, NAME, SURNAME, Expense, load_csv


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    if not CSV_FILE.is_file():
        print(f"error: {CSV_FILE} not found", file=sys.stderr)
        sys.exit(1)

    expenses = load_csv(CSV_FILE)
    print(f"objects created: {Expense.count}")
    print(f"currency: {Expense.currency}")
    for e in expenses[:3]:
        print("  ", e)

    Expense.set_currency("USD")
    print("after Expense.set_currency('USD'):")
    for e in expenses[:3]:
        print("  ", e)
    print("instance dict has no own currency:",
          "currency" not in expenses[0].__dict__)


if __name__ == "__main__":
    main()
