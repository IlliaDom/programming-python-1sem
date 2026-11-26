import json
from datetime import date

NAME = "Nazar Mischuk IT-32"

original = {
    "category": "food",
    "amount": 85.5,
    "date": date(2026, 9, 21),
    "comment": "lunch",
}

def show_error():
    try:
        json.dumps(original)
    except TypeError as error:
        print(f"TypeError: {error}")


def date_default(obj):
    """Викликається json лише для типів, яких він не знає."""
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


def date_hook(data):
    """Читання: рядок вигляду РРРР-ММ-ДД у полі date стає об'єктом date."""
    if isinstance(data.get("date"), str):
        data["date"] = date.fromisoformat(data["date"])
    return data


def way1():
    text = json.dumps(original, default=date_default, ensure_ascii=False)
    print("way 1 JSON:", text)
    restored = json.loads(text, object_hook=date_hook)
    return restored


def dates_to_str(data):
    """Повертає копію словника, де всі date замінено на рядки ISO."""
    return {k: (v.isoformat() if isinstance(v, date) else v) for k, v in data.items()}


def str_to_dates(data):
    """Повертає копію словника, де поле date знову стало об'єктом date."""
    result = dict(data)
    if isinstance(result.get("date"), str):
        result["date"] = date.fromisoformat(result["date"])
    return result


def way2():
    text = json.dumps(dates_to_str(original), ensure_ascii=False)
    print("way 2 JSON:", text)
    restored = str_to_dates(json.loads(text))
    return restored


def main():
    print(NAME)
    show_error()

    restored1 = way1()
    print("way 1 equal:", restored1 == original, "| date type:", type(restored1["date"]).__name__)

    restored2 = way2()
    print("way 2 equal:", restored2 == original, "| date type:", type(restored2["date"]).__name__)


if __name__ == "__main__":
    main()
