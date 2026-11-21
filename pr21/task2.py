import sys

from task1 import CSV_FILE, GROUP, NAME, SURNAME, Expense, load_csv


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    for text in ("2026-09-21", "2026-02-30", "21.09.2026", "abc"):
        print(f"is_valid_date({text!r}): {Expense.is_valid_date(text)}")
    for value in ("85.50", "-5", "abc", "0"):
        print(f"is_valid_amount({value!r}): {Expense.is_valid_amount(value)}")

    for line in ("2026-09-21;food;85.50;lunch",
                 "2026-02-30;food;10;bad date",
                 "2026-09-22;food;abc;bad amount",
                 "2026-09-23;food;10"):
        try:
            print("ok:     ", Expense.from_csv_line(line))
        except ValueError as e:
            print(f"skipped: {line!r} ({e})")

    if not CSV_FILE.is_file():
        print(f"error: {CSV_FILE} not found", file=sys.stderr)
        sys.exit(1)
    print(f"loaded from file: {len(load_csv(CSV_FILE))}")


if __name__ == "__main__":
    main()
