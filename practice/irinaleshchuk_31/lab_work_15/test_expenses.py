import pytest
from expenses import parse_line, total_by_category, load_expenses


def test_parse_line():
    result = parse_line("2026-11-10;food;120.50;lunch")

    assert result == {
        "date": "2026-11-10",
        "category": "food",
        "amount": 120.50,
        "comment": "lunch"
    }


def test_parse_line_wrong_fields():
    with pytest.raises(ValueError):
        parse_line("2026-11-10;food;120.50")


def test_parse_line_invalid_amount():
    with pytest.raises(ValueError):
        parse_line("2026-11-10;food;abc;lunch")


@pytest.mark.parametrize(
    "line, expected_category, expected_amount",
    [
        ("2026-11-10;food;120.50;lunch", "food", 120.50),
        ("2026-11-10;transport;35.00;bus", "transport", 35.00),
        ("2026-11-12;shopping;250.00;clothes", "shopping", 250.00),
        ("2026-11-13;food;150.00;lunch", "food", 150.00),
        ("2026-11-15;entertainment;180.00;cinema", "entertainment", 180.00),
    ]
)
def test_parse_line_parametrized(line, expected_category, expected_amount):
    result = parse_line(line)

    assert result["category"] == expected_category
    assert result["amount"] == expected_amount


def test_load_expenses(tmp_path):
    file_path = tmp_path / "expenses.csv"
    file_path.write_text(
        "2026-11-10;food;100.00;lunch\n"
        "2026-11-11;transport;30.00;bus\n",
        encoding="utf-8"
    )

    records = load_expenses(file_path)

    assert len(records) == 2
    assert total_by_category(records) == {
        "food": 100.00,
        "transport": 30.00
    }


def test_total_by_category_real_file():
    records = load_expenses("data/expenses.csv")

    assert total_by_category(records) == {
        "food": 451.00,
        "transport": 75.00,
        "shopping": 550.00,
        "entertainment": 180.00
    }