import sys

from expense import BASE, DATA_FILE, load_expenses
from exporters import CsvExporter, JsonExporter, TxtExporter
from task1 import GROUP, NAME, SURNAME


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    if not DATA_FILE.is_file():
        print(f"error: {DATA_FILE} not found", file=sys.stderr)
        sys.exit(1)

    expenses = load_expenses()
    for exporter in (CsvExporter(), JsonExporter(), TxtExporter()):
        path = exporter.target(BASE / "report")     # без перевірки типу
        exporter.export(expenses, path)
        print(f"saved: {path.name} ({len(expenses)} records)")


if __name__ == "__main__":
    main()
