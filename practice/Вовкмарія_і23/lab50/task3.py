from abc import abstractmethod
from pathlib import Path
from exporters import Exporter
from data_loader import load_expenses


class IncompleteHtmlExporter(Exporter):
    def extension(self):
        return "html"


try:
    IncompleteHtmlExporter()
except TypeError as error:
    print("incomplete:", error)


class HtmlExporter(Exporter):
    def extension(self):
        return "html"

    def export(self, expenses, path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        headers = ("Дата", "Категорія", "Сума, грн", "Опис")
        header_html = "".join(f"<th>{item}</th>" for item in headers)
        rows = []
        for expense in expenses:
            values = (
                expense.date,
                expense.category,
                f"{expense.amount:.2f}",
                expense.description
            )
            cells = "".join(f"<td>{value}</td>" for value in values)
            rows.append(f"<tr>{cells}</tr>")

        document = f"""<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<title>Звіт витрат Марії Вовк</title>
<style>
body {{ font-family: Arial, sans-serif; margin: 32px; }}
h1 {{ color: #243b53; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ border: 1px solid #999; padding: 8px; text-align: left; }}
th {{ background: #e8eef4; }}
tr:nth-child(even) {{ background: #f5f7fa; }}
</style>
</head>
<body>
<h1>Звіт витрат — Марія Вовк, група І-23</h1>
<p>Кількість записів: {len(expenses)}</p>
<table>
<thead><tr>{header_html}</tr></thead>
<tbody>{''.join(rows)}</tbody>
</table>
</body>
</html>"""
        path.write_text(document, encoding="utf-8")


if __name__ == "__main__":
    print("Maria Vovk, І-23")
    expenses = load_expenses()
    exporter = HtmlExporter()
    target = exporter.target("reports/report")
    exporter.export(expenses, target)
    print(f"saved: {target.name} ({len(expenses)} records)")
