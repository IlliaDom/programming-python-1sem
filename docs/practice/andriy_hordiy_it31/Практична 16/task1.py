import json
from pathlib import Path
expenses_path = Path(__file__).resolve().parent / "data" / "expenses.csv"
expenses_json_path = Path(__file__).resolve().parent / "data" / "expenses.json"
with open(expenses_path, "r", encoding="utf-8") as f:
    expenses_reader = f.readlines()[1:]
expenses_reader = [line.strip().split("|") for line in expenses_reader]
keys = ["date", "category", "amount", "comment"]
expenses_reader = [
    dict(zip(keys, line)) for line in expenses_reader
]
for expense in expenses_reader:
    expense["amount"] = float(expense["amount"])
with open(expenses_json_path, "w", encoding="utf-8") as fjson:
    json.dump(expenses_reader, fjson, ensure_ascii=False, indent=2)
with open(expenses_path, "r", encoding="utf-8") as f:
    counter = len(f.readlines()[1:])
print(f"Всього записів: {counter}")
print(f"Розмір файлу: {expenses_json_path.stat().st_size} байтів")