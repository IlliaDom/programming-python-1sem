
from datetime import datetime

def parse_line(line):
    """Перетворює рядок CSV на словник витрат."""
    parts = line.strip().split(",")

    if len(parts) != 4:
        raise ValueError("Рядок повинен містити 4 поля")

    date, category, amount, note = parts

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Некоректна дата")

    try:
        amount = float(amount)
    except ValueError:
        raise ValueError("Сума повинна бути числом")

    if amount < 0:
        raise ValueError("Сума не може бути від'ємною")

    return {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }

def total_by_category(records):
    """Підраховує витрати за категоріями."""
    totals = {}

    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]

    return {
        category: round(total, 2)
        for category, total in totals.items()
    }

def load_expenses(path):
    """Завантажує коректні записи з CSV-файлу."""
    records = []

    with open(path, "r", encoding="utf-8") as file:
        next(file, None)  # Пропускаємо заголовок

        for line in file:
            if not line.strip():
                continue

            try:
                records.append(parse_line(line))
            except ValueError:
                continue

    return records
