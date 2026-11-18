import pytest
from pathlib import Path

from expenses import parse_line, total_by_category, load_expenses

def test_parse_line_correct():
    result = parse_line("2026-10-01,food,150.50,Обід")

    assert result["date"] == "2026-10-01"
    assert result["category"] == "food"
    assert result["amount"] == 150.50
    assert result["note"] == "Обід"


def test_parse_line_integer_amount():
    result = parse_line("2026-10-02,transport,50,Автобус")

    assert result["amount"] == 50.0


def test_parse_line_empty_note():
    result = parse_line("2026-10-03,books,200,")

    assert result["note"] == ""


def test_parse_line_invalid_amount():
    with pytest.raises(ValueError):
        parse_line("2026-10-01,food,abc,Обід")


def test_parse_line_wrong_number_of_fields():
    with pytest.raises(ValueError):
        parse_line("2026-10-01,food,150")


def test_parse_line_invalid_date():
    with pytest.raises(ValueError):
        parse_line("2026-13-02,coffee,90,Кава")


def test_parse_line_negative_amount():
    with pytest.raises(ValueError):
        parse_line("2026-10-05,transport,-60,Проїзд")


@pytest.mark.parametrize(
    "line, expected_category, expected_amount",
    [
        ("2026-09-30,food,180.0,Обід", "food", 180.0),
        ("2026-10-01,transport,60.0,Проїзд", "transport", 60.0),
        ("2026-10-01,coffee,85.0,Кава", "coffee", 85.0),
        ("2026-10-02,books,250.0,Навчальний посібник", "books", 250.0),
        ("2026-10-04,internet,300.0,Інтернет", "internet", 300.0),
    ]
)
def test_parse_line_parametrized(line, expected_category, expected_amount):
    result = parse_line(line)

    assert result["category"] == expected_category
    assert result["amount"] == expected_amount


def test_load_expenses_tmp_path(tmp_path):
    file_path = tmp_path / "expenses.csv"

    file_path.write_text(
        "date,category,amount,note\n"
        "2026-10-01,food,100,Обід\n"
        "2026-10-02,transport,50,Автобус\n",
        encoding="utf-8"
    )

    records = load_expenses(file_path)

    assert len(records) == 2
    assert records[0]["amount"] == 100.0
    assert records[1]["category"] == "transport"


def test_total_by_category():
    records = [
        {"category": "food", "amount": 100.0},
        {"category": "food", "amount": 50.0},
        {"category": "transport", "amount": 40.0},
    ]

    result = total_by_category(records)

    assert result == {
        "food": 150.0,
        "transport": 40.0
    }

def test_real_expenses_file():
    file_path = Path(__file__).parent / "data" / "expenses.csv"

    records = load_expenses(file_path)

    assert len(records) == 9

    totals = total_by_category(records)

    assert totals == {
        "food": 970.0,
        "transport": 60.0,
        "coffee": 85.0,
        "books": 250.0,
        "internet": 300.0
    }

    assert sum(totals.values()) == 1665.0