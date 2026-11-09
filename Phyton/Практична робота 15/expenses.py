def parse_line(line):
    parts = line.strip().split(";")
    if len(parts) != 4:
        raise ValueError(
            f"Очікується 4 поля, отримано {len(parts)}: {line!r}"
        )
    date, category, amount_str, comment = parts
    try:
        amount = float(amount_str)
    except ValueError as exc:
        raise ValueError(f"Нечислова сума: {amount_str!r}") from exc
    return {
        "date": date,
        "category": category,
        "amount": amount,
        "comment": comment,
    }


def total_by_category(records):
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0.0) + record["amount"]
    return {category: round(total, 2) for category, total in totals.items()}


def load_expenses(path):
    records = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            # Додаємо перевірку на заголовок
            if not stripped or stripped.startswith("#") or "amount" in stripped:
                continue
            records.append(parse_line(stripped))
    return records