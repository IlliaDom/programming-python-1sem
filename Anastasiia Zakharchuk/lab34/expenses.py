def parse_line(line):
    parts = line.strip().split(";")
    if len(parts) != 4:
        raise ValueError("wrong number of fields")
    date, category, amount, comment = parts
    try:
        amount = float(amount)
    except ValueError:
        raise ValueError("amount is not a number")
    return {"date": date, "category": category, "amount": amount, "comment": comment}


def total_by_category(records):
    totals = {}
    for r in records:
        totals[r["category"]] = totals.get(r["category"], 0) + r["amount"]
    for c in totals:
        totals[c] = round(totals[c], 2)
    return totals


def load_expenses(path):
    records = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            records.append(parse_line(line))
    return records
