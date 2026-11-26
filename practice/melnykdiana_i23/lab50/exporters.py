"""Абстрактний контракт і конкретні експортери витрат."""

import csv
import json
from abc import ABC, abstractmethod
from html import escape
from pathlib import Path


class Exporter(ABC):
    @abstractmethod
    def export(self, expenses, path):
        """Записати витрати у файл за вказаним шляхом."""

    def target(self, name):
        return Path(f"{name}.{self.extension()}")

    @abstractmethod
    def extension(self):
        """Повернути розширення файлу без крапки."""


class CsvExporter(Exporter):
    def extension(self):
        return "csv"

    def export(self, expenses, path):
        with Path(path).open("w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "category", "amount", "comment"])
            for expense in expenses:
                writer.writerow([expense.date, expense.category,
                                 f"{expense.amount:.2f}", expense.comment])


class JsonExporter(Exporter):
    def extension(self):
        return "json"

    def export(self, expenses, path):
        data = [expense.as_dict() for expense in expenses]
        with Path(path).open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)


class TxtExporter(Exporter):
    def extension(self):
        return "txt"

    def export(self, expenses, path):
        rows = [(expense.date, expense.category, f"{expense.amount:.2f}", expense.comment)
                for expense in expenses]
        headers = ("Дата", "Категорія", "Сума", "Коментар")
        widths = [max(len(headers[i]), *(len(row[i]) for row in rows)) for i in range(4)]
        with Path(path).open("w", encoding="utf-8") as file:
            file.write(" | ".join(headers[i].ljust(widths[i]) for i in range(4)) + "\n")
            file.write("-+-".join("-" * width for width in widths) + "\n")
            for row in rows:
                file.write(" | ".join(row[i].ljust(widths[i]) for i in range(4)) + "\n")


class HtmlExporter(Exporter):
    def extension(self):
        return "html"

    def export(self, expenses, path):
        rows = "\n".join(
            "<tr>" + "".join(f"<td>{escape(str(value))}</td>" for value in
                              (expense.date, expense.category, f"{expense.amount:.2f}", expense.comment)) + "</tr>"
            for expense in expenses
        )
        document = f"""<!doctype html>
<html lang="uk"><head><meta charset="utf-8"><title>Звіт витрат</title>
<style>body{{font:16px Arial,sans-serif;margin:2rem;color:#183247}}table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid #9aabb7;padding:.5rem;text-align:left}}th{{background:#155e75;color:white}}tr:nth-child(even){{background:#eef4f6}}</style>
</head><body><h1>Звіт витрат</h1><table><thead><tr><th>Дата</th><th>Категорія</th><th>Сума, грн</th><th>Коментар</th></tr></thead><tbody>{rows}</tbody></table></body></html>"""
        Path(path).write_text(document, encoding="utf-8")
