import sys

from expense import BASE, DATA_FILE, load_expenses
from exporters import EXPORTERS
from task1 import GROUP, NAME, SURNAME


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    available = ", ".join(sorted(EXPORTERS))

    if len(sys.argv) != 2:
        print(f"usage: python3 task4.py <format> (available: {available})")
        sys.exit(2)

    fmt = sys.argv[1].lower()
    exporter = EXPORTERS.get(fmt)
    if exporter is None:
        print(f"error: unknown format '{fmt}', available: {available}",
              file=sys.stderr)
        sys.exit(2)

    if not DATA_FILE.is_file():
        print(f"error: {DATA_FILE} not found", file=sys.stderr)
        sys.exit(1)

    expenses = load_expenses()
    path = exporter.target(BASE / "report")
    exporter.export(expenses, path)
    print(f"saved: {path.name} ({len(expenses)} records)")


if __name__ == "__main__":
    main()
