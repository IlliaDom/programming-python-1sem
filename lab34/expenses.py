def parse_line(line):
    parts = line.strip().split(";")

    if len(parts) != 4:
        raise ValueError("Рядок повинен містити 4 поля")

    date, category, amount, comment = parts

    try:
        amount = float(amount)
    except ValueError:
        raise ValueError("Сума повинна бути числом")

    return {
        "date": date,
        "category": category,
        "amount": amount,
        "comment": comment
    }


def total_by_category(records):
    totals = {}

    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]

    return {
        category: round(total, 2)
        for category, total in totals.items()
    }


def load_expenses(path):
    records = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            records.append(parse_line(line))

    return records