import sys
from pathlib import Path

from task1 import GROUP, NAME, SURNAME, Money

DATA_FILE = Path(__file__).resolve().parent / "data" / "expenses.csv"


def load_amounts(path):
    items = []
    with path.open(encoding="utf-8-sig") as f:
        for number, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                items.append(Money(float(line.split(";")[2])))
            except (IndexError, ValueError):
                print(f"warning: line {number} skipped: {line}",
                      file=sys.stderr)
    return items


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    if not DATA_FILE.is_file():
        print(f"error: {DATA_FILE} not found", file=sys.stderr)
        sys.exit(1)

    items = load_amounts(DATA_FILE)
    print("sorted:", ", ".join(str(m) for m in sorted(items)))

    total = sum(items, Money(0))
    print("total (sum with start Money(0)):", total)

    # без початкового значення sum() починає з 0 (int): 0 + Money -> TypeError
    try:
        sum(items)
    except TypeError as e:
        print("sum(items) without start ->", e)

    try:
        Money(10) + 5
    except TypeError as e:
        print("Money(10) + 5 ->", e)


if __name__ == "__main__":
    main()
