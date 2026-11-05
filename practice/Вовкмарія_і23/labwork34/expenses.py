from pathlib import Path


def parse_line(line):
    fields = line.strip().split(";")

    if len(fields) != 4:
        raise ValueError("Рядок повинен містити рівно 4 поля")

    date, category, amount_text, comment = fields

    try:
       amount = float(amount_text)
    except ValueError as exc:
        raise ValueError("Сума повинна бути числом") from exc

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
        totals[category] = totals.get(category, 0.0) + float(record["amount"])

    return {
        category: round(total, 2)
        for category, total in totals.items()
    }


def load_expenses(path):
    records = []

    with Path(path).open("r", encoding="utf-8") as file:
        for line in file:
            cleaned = line.strip()

            if not cleaned or cleaned.startswith("#"):
                continue

            if cleaned.lower().startswith("date;category;amount;"):
                continue

            records.append(parse_line(cleaned))

    return records