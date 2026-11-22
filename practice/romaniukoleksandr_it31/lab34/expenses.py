from pathlib import Path

def parse_line(line):
    data = line.split(";")

    if len(data) < 4:
        raise ValueError(f"do not long enough line(must be 4, but given {len(data)})")
        # return

    try:
        float(data[2])
    except ValueError:
        raise ValueError("price must be a number, not a string")
        # return

    vocabulary = {}

    vocabulary["date"] = data[0]
    vocabulary["category"] = data[1]
    vocabulary["amount"] = float(data[2])
    vocabulary["comment"] = data[3].strip("\n")

    return vocabulary


def total_by_category(records):
    category_total = {}

    for record in records:
        if record["category"] in category_total:
            category_total[record["category"]] += round(record["amount"], 2)
        else:
            category_total[record["category"]] = round(record["amount"], 2)

    return category_total


def load_expenses(path):
    pathed_path = Path(path)
    
    expenses = []
    
    with open(pathed_path, "r", encoding="utf-8") as file:
        for line in file.readlines():
            if line.startswith("#") or not line.strip():
                continue
            arranged = parse_line(line)
            expenses.append(arranged)

    return expenses