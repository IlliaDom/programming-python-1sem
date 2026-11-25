import sys

from data_loader import load_expenses
from exporters import CsvExporter, HtmlExporter, JsonExporter, TxtExporter

EXPORTERS = {
    "csv": CsvExporter(),
    "json": JsonExporter(),
    "txt": TxtExporter(),
    "html": HtmlExporter(),
}


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1 or argv[0] not in EXPORTERS:
        print(f"Невідомий формат. Доступні формати: {', '.join(EXPORTERS)}", file=sys.stderr)
        return 2
    exporter = EXPORTERS[argv[0]]
    expenses = load_expenses()
    path = exporter.target("report")
    exporter.export(expenses, path)
    print(f"saved: {path.name} ({len(expenses)} records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
