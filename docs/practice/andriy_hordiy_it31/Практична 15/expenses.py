def parse_line(line):
    date = line.split('|')[0]
    category = line.split('|')[1]
    amount_str = line.split('|')[2]
    comment = line.split('|')[3]
    try:
        amount = float(amount_str)
    except:
        raise ValueError(f"Ціна має бути числом! Ви ввели: {amount_str}")
    if len(line.split('|')) != 4:
        raise ValueError(f"Рядок має містити 4 знячення! Ви ввели: {len(line.split(','))}")
    return {
        "date:":date,
        "category":category,
        "amount":amount,
        "comment":comment}

def total_by_category(records):
    categories = {}
    for record in records:
        category = record["category"]
        amount = record["amount"]
        if category not in categories:
            categories[category] = 0
        categories[category] += amount
    for category in categories:
        categories[category] = round(categories[category], 2)

    return categories


def load_expenses(path):
    records = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("Date|"):
                continue
            records.append(parse_line(line))

    return records