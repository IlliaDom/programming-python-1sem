"""Завдання 3. Неповна і завершена реалізація HTML-експортера."""

import csv
from pathlib import Path
from expense import Expense
from exporters import Exporter, HtmlExporter


class IncompleteHtmlExporter(Exporter):
    def extension(self):
        return "html"


def main():
    try:
        IncompleteHtmlExporter()
    except TypeError as error:
        print(f"Неповний експортер: {error}")
    with Path(__file__).with_name("expenses.csv").open(encoding="utf-8", newline="") as file:
        expenses = [Expense.from_dict(row) for row in csv.DictReader(file)]
    exporter = HtmlExporter()
    path = Path(__file__).parent / "report.html"
    exporter.export(expenses, path)
    print(f"saved: {path.name} ({len(expenses)} records)")


if __name__ == "__main__":
    main()
