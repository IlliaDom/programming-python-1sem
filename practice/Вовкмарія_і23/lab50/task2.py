from data_loader import load_expenses
from exporters import CsvExporter, JsonExporter, TxtExporter


def main():
    print("Maria Vovk, І-23")
    expenses = load_expenses()
    exporters = [CsvExporter(), JsonExporter(), TxtExporter()]

    for exporter in exporters:
        path = exporter.target("reports/report")
        exporter.export(expenses, path)
        print(f"saved: {path.name} ({len(expenses)} records)")


if __name__ == "__main__":
    main()
