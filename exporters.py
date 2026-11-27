
from abc import ABC, abstractmethod
from pathlib import Path


class Exporter(ABC):
    @abstractmethod
    def export(self, expenses, path):
        """Записати витрати у файл."""

    def target(self, name):
        return Path(f"{name}.{self.extension()}")

    @abstractmethod
    def extension(self):
        """Повернути розширення файлу без крапки."""



import csv
import json


def load_expenses():
    from expense import Expense

    expenses = []

    with open("data/expenses.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row in reader:
            expense = Expense(
                row["date"],
                row["category"],
                float(row["amount"]),
                row.get("comment", "")
            )
            expenses.append(expense)

    return expenses


class CsvExporter(Exporter):
    def extension(self):
        return "csv"

    def export(self, expenses, path):
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["date", "category", "amount", "comment"])

            for expense in expenses:
                writer.writerow([
                    expense.date,
                    expense.category,
                    expense.amount,
                    expense.comment
                ])


class JsonExporter(Exporter):
    def extension(self):
        return "json"

    def export(self, expenses, path):
        data = []

        for expense in expenses:
            data.append({
                "date": expense.date,
                "category": expense.category,
                "amount": expense.amount,
                "comment": expense.comment
            })

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


class TxtExporter(Exporter):
    def extension(self):
        return "txt"

    def export(self, expenses, path):
        lines = ["ЗВІТ ПРО ВИТРАТИ", ""]

        total = 0

        for expense in expenses:
            lines.append(
                f"{expense.date} | {expense.category} | "
                f"{expense.amount:.2f} грн | {expense.comment}"
            )
            total += expense.amount

        lines.append("")
        lines.append(f"Загальна сума: {total:.2f} грн")

        with open(path, "w", encoding="utf-8") as file:
            file.write("\n".join(lines))
