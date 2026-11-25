from abc import ABC, abstractmethod
import csv
import html
import json
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
    def export(self, expenses, path):
        rows = [expense.as_dict() for expense in expenses]
        with Path(path).open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["category", "amount", "currency"])
            writer.writeheader()
            writer.writerows(rows)

    def extension(self):
        return "csv"


class JsonExporter(Exporter):
    def export(self, expenses, path):
        Path(path).write_text(
            json.dumps([expense.as_dict() for expense in expenses], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def extension(self):
        return "json"


class TxtExporter(Exporter):
    def export(self, expenses, path):
        rows = [(e.category, f"{e.amount:g}", e.currency) for e in expenses]
        headers = ("Category", "Amount", "Currency")
        widths = [max(len(headers[i]), *(len(row[i]) for row in rows)) for i in range(3)]
        line = "+-" + "-+-".join("-" * width for width in widths) + "-+"
        def format_row(row):
            return "| " + " | ".join(value.ljust(widths[i]) for i, value in enumerate(row)) + " |"
        content = [line, format_row(headers), line]
        content.extend(format_row(row) for row in rows)
        content.append(line)
        Path(path).write_text("\n".join(content) + "\n", encoding="utf-8")

    def extension(self):
        return "txt"


class HtmlExporter(Exporter):
    def export(self, expenses, path):
        rows = "\n".join(
            "<tr>" + "".join(f"<td>{html.escape(str(value))}</td>" for value in e.as_dict().values()) + "</tr>"
            for e in expenses
        )
        document = (
            "<!doctype html><html lang='uk'><meta charset='utf-8'><title>Звіт витрат</title>"
            "<style>body{font:16px system-ui;margin:2rem}table{border-collapse:collapse}"
            "th,td{border:1px solid #999;padding:.5rem 1rem;text-align:left}th{background:#eee}</style>"
            "<h1>Звіт витрат</h1><table><thead><tr><th>Категорія</th><th>Сума</th>"
            f"<th>Валюта</th></tr></thead><tbody>{rows}</tbody></table></html>"
        )
        Path(path).write_text(document, encoding="utf-8")

    def extension(self):
        return "html"
