import json
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parent
print("Anatolii Kurotych, PZ-11")

original = {
    "owner": "Anatolii Kurotych",
    "created": date.today(),
    "deadline": date(2026, 12, 1)
}

try:
    json.dumps(original)
except TypeError as error:
    print("TypeError:", error)

def date_to_iso(value):
    if isinstance(value, date):
        return value.isoformat()
    raise TypeError(f"Unsupported type: {type(value).__name__}")

with (BASE / "date_default.json").open("w", encoding="utf-8") as file:
    json.dump(original, file, default=date_to_iso, indent=2, ensure_ascii=False)

def prepare(value):
    if isinstance(value, date):
        return {"__type__": "date", "value": value.isoformat()}
    if isinstance(value, dict):
        return {key: prepare(item) for key, item in value.items()}
    if isinstance(value, list):
        return [prepare(item) for item in value]
    return value

def restore(value):
    if isinstance(value, dict):
        if value.get("__type__") == "date":
            return date.fromisoformat(value["value"])
        return {key: restore(item) for key, item in value.items()}
    if isinstance(value, list):
        return [restore(item) for item in value]
    return value

with (BASE / "date_custom.json").open("w", encoding="utf-8") as file:
    json.dump(prepare(original), file, indent=2, ensure_ascii=False)
with (BASE / "date_custom.json").open(encoding="utf-8") as file:
    restored = restore(json.load(file))

print("equal:", restored == original)
print("date type restored:", isinstance(restored["created"], date))
