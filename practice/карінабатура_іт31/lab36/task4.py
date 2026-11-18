import json
from datetime import date
from pathlib import Path

STUDENT_INFO = "Batura Karina, IT-31"
TEST_FILE = Path("data/date_test.json")


def serialize_date_default(value):
    if isinstance(value, date):
        return value.isoformat()
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def prepare_for_json(record: dict) -> dict:
    """Явно перетворює всі об'єкти date у словнику на рядки ISO."""
    result = {}
    for key, value in record.items():
        if isinstance(value, date):
            result[key] = value.isoformat()
        else:
            result[key] = value
    return result


def restore_from_json(record: dict, date_fields: tuple[str, ...] = ("date", "deadline")) -> dict:
    """Відновлює рядки ISO назад в об'єкти datetime.date."""
    result = dict(record)
    for field in date_fields:
        if field in result and isinstance(result[field], str):
            result[field] = date.fromisoformat(result[field])
    return result


def main() -> None:
    print(STUDENT_INFO)

    original = {
        "title": "Здати лабораторну №36",
        "date": date(2026, 11, 16),
        "deadline": date(2026, 11, 20),
        "completed": False,
    }

    try:
        json.dumps(original)
    except TypeError as err:
        print(f"Caught expected error: TypeError: {err}")

    # Спосіб 1: Параметр default=
    json_str = json.dumps(original, default=serialize_date_default, ensure_ascii=False)
    print("Method 1 (default=):", json_str)

    # Спосіб 2: Власні функції перетворення до запису та після читання
    prepared = prepare_for_json(original)
    with TEST_FILE.open("w", encoding="utf-8") as file:
        json.dump(prepared, file, indent=2, ensure_ascii=False)

    with TEST_FILE.open("r", encoding="utf-8") as file:
        raw_loaded = json.load(file)

    restored = restore_from_json(raw_loaded)
    print("Method 2 (restored == original):", restored == original)
    print("Type of restored['date']:", type(restored["date"]))


if __name__ == "__main__":
    main()