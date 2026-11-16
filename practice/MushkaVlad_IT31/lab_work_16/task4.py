import json
from datetime import date

print("Vlad Mushka, IT31")

data = {
    "event": "expense",
    "date": date.today()
}

# Спроба звичайної серіалізації
try:
    print(json.dumps(data))
except TypeError as error:
    print("TypeError:", error)

# Спосіб 1: параметр default
json_text = json.dumps(
    data,
    default=lambda value: value.isoformat()
)

restored = json.loads(json_text)
restored["date"] = date.fromisoformat(restored["date"])

print("Method 1:", restored == data)

# Спосіб 2: власні функції
def serialize(obj):
    return {
        "event": obj["event"],
        "date": obj["date"].isoformat()
    }

def deserialize(obj):
    return {
        "event": obj["event"],
        "date": date.fromisoformat(obj["date"])
    }

with open("date.json", "w", encoding="utf-8") as file:
    json.dump(serialize(data), file, indent=2)

with open("date.json", "r", encoding="utf-8") as file:
    restored = deserialize(json.load(file))

print("Method 2:", restored == data)
print("Date type:", type(restored["date"]))