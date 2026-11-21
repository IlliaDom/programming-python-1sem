import sys

from expense import BASE, DATA_FILE, load_expenses
from exporters import Exporter, HtmlExporter
from task1 import GROUP, NAME, SURNAME


class IncompleteHtmlExporter(Exporter):
    """Реалізує лише extension(): export() відсутній."""
    def extension(self):
        return "html"


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    try:
        IncompleteHtmlExporter()
    except TypeError as error:
        print("error:", error)

    if not DATA_FILE.is_file():
        print(f"error: {DATA_FILE} not found", file=sys.stderr)
        sys.exit(1)
    expenses = load_expenses()
    exporter = HtmlExporter()           # повна реалізація
    path = exporter.target(BASE / "report")
    exporter.export(expenses, path)
    print(f"saved: {path.name} ({len(expenses)} records)")


if __name__ == "__main__":
    main()
