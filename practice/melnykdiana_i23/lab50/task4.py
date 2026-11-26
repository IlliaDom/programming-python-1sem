"""Завдання 4. Вибір експортера за аргументом командного рядка."""

import argparse
import csv
from pathlib import Path
from expense import Expense
from exporters import CsvExporter, JsonExporter, TxtExporter, HtmlExporter


def main():
    exporters = {exporter.extension(): exporter for exporter in
                 (CsvExporter(), JsonExporter(), TxtExporter(), HtmlExporter())}
    parser = argparse.ArgumentParser(description="Експорт особистих витрат")
    parser.add_argument("format", help="Формат звіту")
    args = parser.parse_args()
    if args.format not in exporters:
        print(f"Невідомий формат: {args.format}. Доступні формати: {', '.join(sorted(exporters))}")
        return 2
    with Path(__file__).with_name("expenses.csv").open(encoding="utf-8", newline="") as file:
        expenses = [Expense.from_dict(row) for row in csv.DictReader(file)]
    exporter = exporters[args.format]
    path = Path(__file__).parent / f"report.{exporter.extension()}"
    exporter.export(expenses, path)
    print(f"saved: {path.name} ({len(expenses)} records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
