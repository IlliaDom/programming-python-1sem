import json
from datetime import date

print("Лещук Ірина, IT-31")

data = {
    "owner": "Лещук Ірина",
    "group": "IT-31",
    "date": date.today(),
    "category": "food"
}

# Спроба звичайної серіалізації
try:
    json.dumps(data)
except TypeError as error:
    print("TypeError:", error)

# Спосіб 1: використання default
def date_converter(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError("Unsupported type")

json_text = json.dumps(data, default=date_converter, ensure_ascii=False)
print("Спосіб 1:", json_text)

# Спосіб 2: власна серіалізація та десеріалізація
def serialize(obj):
    result = obj.copy()
    if isinstance(result.get("date"), date):
        result["date"] = result["date"].isoformat()
    return result

def deserialize(obj):
    result = obj.copy()
    result["date"] = date.fromisoformat(result["date"])
    return result

saved_data = serialize(data)

with open("date_data.json", "w", encoding="utf-8") as file:
    json.dump(saved_data, file, indent=2, ensure_ascii=False)

with open("date_data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

restored_data = deserialize(loaded_data)

print("Спосіб 2:", restored_data)
print("Дані збігаються:", data == restored_data)
print("Дата є об'єктом date:", isinstance(restored_data["date"], date))