from pathlib import Path
from tabulate import tabulate
from collections import defaultdict

NAME_SURNAME = "Oleksandra Romanich"
GROUP = "IT-32"

def main():
    print(f"{NAME_SURNAME}, {GROUP}")
    
    file_path = Path(__file__).parent / "data" / "expenses.csv"
    
    categories = defaultdict(lambda: {"count": 0, "total": 0.0})
    total_all = 0.0

    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(";")
            if len(parts) == 4:
                try:
                    category = parts[1].strip()
                    amount = float(parts[2].strip())
                    categories[category]["count"] += 1
                    categories[category]["total"] += amount
                    total_all += amount
                except ValueError:
                    continue

    table_data = []
    total_count = 0

    for cat, data in categories.items():
        table_data.append([cat, data["count"], data["total"]])
        total_count += data["count"]

    table_data.append(["TOTAL", total_count, total_all])

    print(tabulate(table_data, headers=["category", "count", "total"], tablefmt="github", floatfmt=".2f"))

if __name__ == "__main__":
    main()