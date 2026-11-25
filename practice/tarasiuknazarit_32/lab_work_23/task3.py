from data_loader import load_expenses
from exporters import Exporter, HtmlExporter


class IncompleteHtmlExporter(Exporter):
    def extension(self):
        return "html"


try:
    IncompleteHtmlExporter()
except TypeError as error:
    print("error:", error)

expenses = load_expenses()
exporter = HtmlExporter()
path = exporter.target("report")
exporter.export(expenses, path)
print(f"saved: {path.name} ({len(expenses)} records)")
