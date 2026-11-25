from config import GROUP, STUDENT_NAME
from data_loader import load_expenses
from exporters import CsvExporter, JsonExporter, TxtExporter


def main():
    expenses = load_expenses()
    print(f"{STUDENT_NAME}, {GROUP}")
    for exporter in (CsvExporter(), JsonExporter(), TxtExporter()):
        path = exporter.target("report")
        exporter.export(expenses, path)
        print(f"saved: {path.name} ({len(expenses)} records)")


if __name__ == "__main__":
    main()
