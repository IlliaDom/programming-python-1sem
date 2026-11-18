import csv
import json
from pathlib import Path

STUDENT_INFO = "Batura Karina, IT-31"
CSV_PATH = Path("data/expenses.csv")
JSON_PATH = Path("data/expenses.json")


def main() -> None:
    print(STUDENT_INFO)

    expenses = []
    with CSV_PATH.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",")
        for row in reader:
            expenses.append({
                "date": row["date"].strip(),
                "category": row["category"].strip(),
                "amount": float(row["amount"]),
                "comment": row.get("comment", "").strip(),
            })

    with JSON_PATH.open("w", encoding="utf-8") as json_file:
        json.dump(expenses, json_file, indent=2, ensure_ascii=False)

    file_size = JSON_PATH.stat().st_size
    print(f"records: {len(expenses)}")
    print(f"saved: {JSON_PATH.as_posix()} ({file_size} bytes)")


if __name__ == "__main__":
    main()