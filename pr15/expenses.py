"""Функції для роботи з файлом витрат. Жодних print — лише повернення результату."""


def parse_line(line):
    """Перетворює рядок 'дата;категорія;сума;коментар' на словник.

    Генерує ValueError, якщо полів не 4 або сума не є числом.
    """
    parts = line.strip().split(";")
    if len(parts) != 4:
        raise ValueError(f"Очікувалось 4 поля, отримано {len(parts)}: {line!r}")

    date, category, amount_text, comment = parts
    try:
        amount = float(amount_text)
    except ValueError:
        raise ValueError(f"Сума не є числом: {amount_text!r}")

    return {
        "date": date,
        "category": category,
        "amount": amount,
        "comment": comment,
    }


def total_by_category(records):
    """Повертає словник {категорія: сума}, суми округлені до двох знаків."""
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return {category: round(total, 2) for category, total in totals.items()}


def load_expenses(path):
    """Читає файл, пропускає коментарі (#) та порожні рядки, повертає список словників."""
    records = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            records.append(parse_line(line))
    return records
