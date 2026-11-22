import csv
import json
from pathlib import Path

print("Karina Pikul, IT-32")

BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "data" / "expenses.csv"
JSON_FILE = BASE_DIR / "data" / "expenses.json"

expenses = []

with open(CSV_FILE, "r", encoding="utf-8") as file:
    for line in file:
        if line.startswith("#") or not line.strip():
            continue

        date, category, amount, note = line.strip().split(";")

        expenses.append({
            "date": date,
            "category": category,
            "amount": float(amount),
            "comment": note
        })

with open(JSON_FILE, "w", encoding="utf-8") as file:
    json.dump(expenses, file, indent=2, ensure_ascii=False)

file_size = JSON_FILE.stat().st_size

print(f"Кількість записів: {len(expenses)}")
print(f"Розмір JSON-файлу: {file_size} байт")
print(f"Файл збережено: {JSON_FILE}")
