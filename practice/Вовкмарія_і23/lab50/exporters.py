from abc import ABC, abstractmethod
from pathlib import Path
import csv
import json


class Exporter(ABC):
    @abstractmethod
    def export(self, expenses, path):
        pass

    def target(self, name):
        return Path(f"{name}.{self.extension()}")

    @abstractmethod
    def extension(self):
        pass


class CsvExporter(Exporter):
    def extension(self):
        return "csv"

    def export(self, expenses, path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8-sig", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["date", "category", "amount", "description"],
                delimiter=";"
            )
            writer.writeheader()
            writer.writerows(expense.to_dict() for expense in expenses)


class JsonExporter(Exporter):
    def extension(self):
        return "json"

    def export(self, expenses, path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        data = [expense.to_dict() for expense in expenses]
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=4),
            encoding="utf-8"
        )


class TxtExporter(Exporter):
    def extension(self):
        return "txt"

    def export(self, expenses, path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        rows = [
            ("Дата", "Категорія", "Сума, грн", "Опис"),
            ("-" * 10, "-" * 16, "-" * 10, "-" * 20)
        ]
        for expense in expenses:
            rows.append((
                expense.date,
                expense.category,
                f"{expense.amount:.2f}",
                expense.description
            ))
        widths = [max(len(row[i]) for row in rows) for i in range(4)]
        lines = [
            " | ".join(value.ljust(widths[i]) for i, value in enumerate(row))
            for row in rows
        ]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
