import pytest
from expenses import parse_line
from pathlib import Path
from expenses import load_expenses, total_by_category

def test_parse_line_valid():
    record = parse_line("2026-09-21;food;85.50;lunch")

    assert record["date"] == "2026-09-21"
    assert record["category"] == "food"
    assert record["amount"] == 85.5
    assert record["comment"] == "lunch"


def test_parse_line_amount():
    record = parse_line("2026-09-22;transport;25.00;bus")

    assert record["amount"] == 25.0


def test_parse_line_category():
    record = parse_line("2026-09-23;coffee;40.00;latte")

    assert record["category"] == "coffee"


def test_parse_line_wrong_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50")


def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;abc;lunch")


@pytest.mark.parametrize(
    "line, expected_category, expected_amount",
    [
        ("2026-10-20;РџСЂРѕРґСѓРєС‚Рё;500;РџРѕРєСѓРїРєРё", "РџСЂРѕРґСѓРєС‚Рё", 500.0),
        ("2026-10-21;РўСЂР°РЅСЃРїРѕСЂС‚;100;РџРѕС—Р·РґРєР°", "РўСЂР°РЅСЃРїРѕСЂС‚", 100.0),
        ("2026-10-21;РўСЂР°РЅСЃРїРѕСЂС‚;100;РџРѕС—Р·РґРєР°", "РўСЂР°РЅСЃРїРѕСЂС‚", 100.0),
        ("2026-10-22;РћР±С–Рґ;180;РћР±С–Рґ", "РћР±С–Рґ", 180.0),
        ("2026-10-22;РњРѕР±С–Р»СЊРЅРёР№ Р·РІ'СЏР·РѕРє;250;РџРѕРїРѕРІРЅРµРЅРЅСЏ СЂР°С…СѓРЅРєСѓ", "РњРѕР±С–Р»СЊРЅРёР№ Р·РІ'СЏР·РѕРє", 250.0),
    ]
)
def test_parse_line_parametrized(line, expected_category, expected_amount):
    record = parse_line(line)

    assert record["category"] == expected_category
    assert record["amount"] == expected_amount


def test_load_and_total_expenses(tmp_path):
    path = tmp_path / "expenses.csv"

    path.write_text(
        "2026-10-20;food;85.50;lunch\n"
        "2026-10-21;food;14.50;coffee\n",
        encoding="utf-8"
    )

    records = load_expenses(path)

    assert len(records) == 2

    totals = total_by_category(records)

    assert totals == {"food": 100.0}


def test_total_by_category_real_file():
    records = load_expenses(Path("data/expenses.csv"))

    totals = total_by_category(records)

    assert totals == {
        "Продукти": 500.0,
        "Транспорт": 200.0,
        "Обід": 180.0,
        "Мобільний зв'язок": 250.0,
        "Канцелярія": 120.0,
        "Вода": 30.0,
        "Перекус": 70.0,
        "Проїзд": 50.0,
        "Фільм": 200.0,
        "Книга": 350.0,
        "Побутові товари": 300.0,
        "Кава": 80.0
    }
