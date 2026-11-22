import json
from datetime import date
from pathlib import Path

print("Karina Pikul, IT-32")

BASE_DIR = Path(__file__).parent

today = date.today()

def date_serializer(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Тип {type(obj)} не підтримується")


data = {
    "event": "Практична робота",
    "date": today
}

try:
    json.dumps(data)
except TypeError as error:
    print("Помилка серіалізації:", error)

json_text = json.dumps(
    data,
    default=date_serializer,
    indent=2,
    ensure_ascii=False
)

with open(BASE_DIR / "date_default.json", "w", encoding="utf-8") as file:
    file.write(json_text)

print("Спосіб 1: дату збережено через default=")

data_manual = {
    "event": "Практична робота",
    "date": today.isoformat()
}

with open(BASE_DIR / "date_manual.json", "w", encoding="utf-8") as file:
    json.dump(data_manual, file, indent=2, ensure_ascii=False)

with open(BASE_DIR / "date_manual.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

loaded_data["date"] = date.fromisoformat(loaded_data["date"])

assert loaded_data["date"] == today
assert isinstance(loaded_data["date"], date)

print("Спосіб 2: дату збережено та відновлено")
print("Перевірка успішна:", loaded_data["date"])
