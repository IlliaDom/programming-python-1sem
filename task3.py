
from exporters import Exporter, load_expenses


class IncompleteHtmlExporter(Exporter):
    def extension(self):
        return "html"


print("Перевірка незавершеного класу:")

try:
    IncompleteHtmlExporter()
except TypeError as error:
    print("error:", error)


class HtmlExporter(Exporter):
    def extension(self):
        return "html"

    def export(self, expenses, path):
        rows = ""

        for expense in expenses:
            rows += f"""
            <tr>
                <td>{expense.date}</td>
                <td>{expense.category}</td>
                <td>{expense.amount:.2f}</td>
                <td>{expense.comment}</td>
            </tr>
            """

        html = f"""
        <!DOCTYPE html>
        <html lang="uk">
        <head>
            <meta charset="UTF-8">
            <title>Звіт про витрати</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 30px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                }}
                th, td {{
                    border: 1px solid #999;
                    padding: 10px;
                    text-align: left;
                }}
                th {{
                    background: #eeeeee;
                }}
            </style>
        </head>
        <body>
            <h1>Звіт про витрати</h1>
            <table>
                <tr>
                    <th>Дата</th>
                    <th>Категорія</th>
                    <th>Сума</th>
                    <th>Коментар</th>
                </tr>
                {rows}
            </table>
        </body>
        </html>
        """

        with open(path, "w", encoding="utf-8") as file:
            file.write(html)


expenses = load_expenses()
exporter = HtmlExporter()

path = exporter.target("report")
exporter.export(expenses, path)

print(f"saved: {path} ({len(expenses)} records)")
