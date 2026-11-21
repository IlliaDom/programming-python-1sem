import csv
import json
from abc import ABC, abstractmethod
from html import escape
from pathlib import Path


class Exporter(ABC):
    @abstractmethod
    def export(self, expenses, path):
        """Write expenses to the file at path."""

    def target(self, name):
        return Path(f"{name}.{self.extension()}")

    @abstractmethod
    def extension(self):
        """Return file extension without dot."""


class CsvExporter(Exporter):
    def extension(self):
        return "csv"

    def export(self, expenses, path):
        with Path(path).open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["date", "category", "amount", "comment"])
            for e in expenses:
                writer.writerow([e.date, e.category, f"{e.amount:.2f}",
                                 e.comment])


class JsonExporter(Exporter):
    def extension(self):
        return "json"

    def export(self, expenses, path):
        data = [{"date": e.date, "category": e.category,
                 "amount": e.amount, "comment": e.comment} for e in expenses]
        with Path(path).open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


class TxtExporter(Exporter):
    def extension(self):
        return "txt"

    def export(self, expenses, path):
        lines = [f"{'date':<12}{'category':<14}{'amount':>10}  comment",
                 "-" * 48]
        for e in expenses:
            lines.append(f"{e.date:<12}{e.category:<14}"
                         f"{e.amount:>10.2f}  {e.comment}")
        Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


class HtmlExporter(Exporter):
    def extension(self):
        return "html"

    def export(self, expenses, path):
        rows = "\n".join(
            f"    <tr><td>{escape(e.date)}</td><td>{escape(e.category)}</td>"
            f"<td>{e.amount:.2f}</td><td>{escape(e.comment)}</td></tr>"
            for e in expenses)
        page = (
            "<!doctype html>\n<html lang=\"uk\">\n<head>\n"
            "  <meta charset=\"utf-8\">\n  <title>Expenses report</title>\n"
            "  <style>table{border-collapse:collapse}"
            "td,th{border:1px solid #888;padding:4px 10px}</style>\n"
            "</head>\n<body>\n  <h1>Expenses</h1>\n  <table>\n"
            "    <tr><th>date</th><th>category</th><th>amount</th>"
            "<th>comment</th></tr>\n"
            f"{rows}\n  </table>\n</body>\n</html>\n")
        Path(path).write_text(page, encoding="utf-8")

EXPORTERS = {
    "csv": CsvExporter(),
    "json": JsonExporter(),
    "txt": TxtExporter(),
    "html": HtmlExporter(),
}
