"""Функції для роботи з файлом витрат. Жодного print — лише return."""
from pathlib import Path


def parse_line(line):
    """'2026-09-21;food;85.50;lunch' -> словник. Інакше ValueError."""
    parts = line.strip().split(";")
    if len(parts) != 4:
        raise ValueError(f"expected 4 fields, got {len(parts)}: {line!r}")
    date, category, amount, comment = (p.strip() for p in parts)
    try:
        value = float(amount)
    except ValueError:
        raise ValueError(f"amount is not a number: {amount!r}") from None
    return {"date": date, "category": category,
            "amount": value, "comment": comment}


def total_by_category(records):
    """Список словників -> {category: сума, округлена до 2 знаків}."""
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0.0) + record["amount"]
    return {category: round(total, 2) for category, total in totals.items()}


def load_expenses(path):
    """Читає файл, пропускає коментарі та порожні рядки."""
    records = []
    with Path(path).open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            records.append(parse_line(line))
    return records
