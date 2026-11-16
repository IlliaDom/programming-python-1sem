import json
from datetime import date

print("Nikita Krilovets, IT-31")

data = {
    "name": "Nikita",
    "date": date.today()
}

try:
    json.dumps(data)

except TypeError as error:
    print("TypeError:", error)

def date_serializer(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError("Unsupported type")

json_string = json.dumps(data, default=date_serializer)

restored = json.loads(json_string)
restored["date"] = date.fromisoformat(restored["date"])

print("Method 1:", restored == data)

def prepare_dates(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {key: prepare_dates(value) for key, value in obj.items()}
    if isinstance(obj, list):
        return [prepare_dates(value) for value in obj]
    return obj

def restore_dates(obj):
    if isinstance(obj, dict):
        return {key: restore_dates(value) for key, value in obj.items()}
    if isinstance(obj, list):
        return [restore_dates(value) for value in obj]
    if isinstance(obj, str):
        try:
            return date.fromisoformat(obj)
        except ValueError:
            return obj
    return obj

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(prepare_dates(data), file, indent=2, ensure_ascii=False)

with open("data.json", "r", encoding="utf-8") as file:
    restored_data = restore_dates(json.load(file))

print("Method 2:", restored_data == data)
print("Date type:", type(restored_data["date"]))
