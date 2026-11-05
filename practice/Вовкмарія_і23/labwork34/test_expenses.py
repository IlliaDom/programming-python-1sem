from pathlib import Path

import pytest

from expenses import parse_line, total_by_category, load_expenses


def test_parse_line_valid():
    result = parse_line("2026-09-21;Food;150;Обід")

    assert result["date"] == "2026-09-21"
    assert result["category"] == "Food"
    assert result["amount"] == 150.0
    assert result["comment"] == "Обід"


def test_parse_line_another_amount():
    result = parse_line("2026-09-22;Transport;40;Автобус")

    assert result["amount"] == 40.0


def test_parse_line_decimal_amount():
    result = parse_line("2026-09-23;Study;85.50;Канцтовари")

    assert result["amount"] == 85.50


def test_parse_line_wrong_number_of_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;Food;150")


def test_parse_line_invalid_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;Food;abc;Обід")


@pytest.mark.parametrize(
    "line, expected_date, expected_category, expected_amount",
    [
        ("2026-09-21;Food;150;Обід", "2026-09-21", "Food", 150.0),
        ("2026-09-22;Transport;40;Автобус", "2026-09-22", "Transport", 40.0),
        ("2026-09-23;Study;85;Канцтовари", "2026-09-23", "Study", 85.0),
        ("2026-09-24;Entertainment;200;Кіно", "2026-09-24", "Entertainment", 200.0),
        ("2026-09-26;Food;220;Продукти", "2026-09-26", "Food", 220.0),
    ],
)
def test_parse_real_expense_rows(line, expected_date, expected_category, expected_amount):
    result = parse_line(line)

    assert result["date"] == expected_date
    assert result["category"] == expected_category
    assert result["amount"] == expected_amount


def test_total_by_category_with_tmp_path(tmp_path):
    file_path = tmp_path / "expenses.csv"
    file_path.write_text(
        "2026-09-21;Food;60;Обід\n"
        "2026-09-22;Food;40;Вечеря\n",
        encoding="utf-8",
    )

    records = load_expenses(file_path)

    assert total_by_category(records) == {"Food": 100.0}


def test_real_expenses_file_totals():
    data_path = Path(__file__).parent / "data" / "expenses.csv"

    records = load_expenses(data_path)

    assert len(records) == 13
    assert total_by_category(records) == {
        "Food": 1035.0,
        "Transport": 120.0,
        "Study": 145.0,
        "Entertainment": 200.0,
    }