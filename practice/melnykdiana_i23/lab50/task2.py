"""Завдання 2. Експорт витрат у три формати одним циклом."""

import csv
from pathlib import Path
from expense import Expense
from exporters import CsvExporter, JsonExporter, TxtExporter


def load_expenses():
    with Path(__file__).with_name("expenses.csv").open(encoding="utf-8", newline="") as file:
        return [Expense.from_dict(row) for row in csv.DictReader(file)]


def main():
    expenses = load_expenses()
    output_base = Path(__file__).parent / "report"
    exporters = [CsvExporter(), JsonExporter(), TxtExporter()]
    print("Ivan Petrenko, PZ-11")  # Зразок із завдання; за потреби замініть на свої дані.
    for exporter in exporters:
        path = output_base.with_suffix(f".{exporter.extension()}")
        exporter.export(expenses, path)
        print(f"saved: {path.name} ({len(expenses)} records)")


if __name__ == "__main__":
    main()
