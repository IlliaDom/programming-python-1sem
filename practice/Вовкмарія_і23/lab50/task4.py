import sys
from data_loader import load_expenses
from exporters import CsvExporter, JsonExporter, TxtExporter


def main():
    print("Maria Vovk, І-23")
    available = {
        "csv": CsvExporter(),
        "json": JsonExporter(),
        "txt": TxtExporter()
    }

    if len(sys.argv) != 2 or sys.argv[1] not in available:
        print("Доступні формати: " + ", ".join(available), file=sys.stderr)
        print("Використання: python task4.py <csv|json|txt>", file=sys.stderr)
        return 2

    extension = sys.argv[1]
    expenses = load_expenses()
    exporter = available[extension]
    path = exporter.target("reports/user_report")
    exporter.export(expenses, path)
    print(f"saved: {path.name} ({len(expenses)} records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
