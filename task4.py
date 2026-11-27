
import sys

from exporters import (
    load_expenses,
    CsvExporter,
    JsonExporter,
    TxtExporter
)

from task3 import HtmlExporter


EXPORTERS = {
    "csv": CsvExporter(),
    "json": JsonExporter(),
    "txt": TxtExporter(),
    "html": HtmlExporter()
}


def main():
    if len(sys.argv) < 2:
        print("Вкажіть формат: csv, json, txt або html")
        sys.exit(2)

    format_name = sys.argv[1].lower()

    if format_name not in EXPORTERS:
        print(
            "Невідомий формат:",
            format_name
        )
        print(
            "Доступні формати:",
            ", ".join(sorted(EXPORTERS))
        )
        sys.exit(2)

    expenses = load_expenses()
    exporter = EXPORTERS[format_name]

    path = exporter.target("report")
    exporter.export(expenses, path)

    print(f"saved: {path} ({len(expenses)} records)")


if __name__ == "__main__":
    main()
