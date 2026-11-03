import pytest
from expenses import parse_line, total_by_category, load_expenses


def test_parse_line():
    result = parse_line("2026-09-21;food;85.50;lunch")

    assert result == {
        "date": "2026-09-21",
        "category": "food",
        "amount": 85.50,
        "comment": "lunch"
    }


def test_parse_line_wrong_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50")


def test_parse_line_invalid_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;abc;lunch")


@pytest.mark.parametrize(
    "line, expected_category, expected_amount",
    [
        ("2026-09-21;food;120;lunch", "food", 120.0),
        ("2026-09-22;transport;30;bus", "transport", 30.0),
        ("2026-09-23;coffee;60;coffee", "coffee", 60.0),
        ("2026-09-24;entertainment;100;movie", "entertainment", 100.0),
        ("2026-09-25;mobile;100;phone", "mobile", 100.0),
    ]
)
def test_parse_line_parametrize(line, expected_category, expected_amount):
    result = parse_line(line)

    assert result["category"] == expected_category
    assert result["amount"] == expected_amount


def test_total_by_category():
    records = [
        {"category": "food", "amount": 100.0},
        {"category": "food", "amount": 50.0},
        {"category": "transport", "amount": 30.0},
    ]

    assert total_by_category(records) == {
        "food": 150.0,
        "transport": 30.0
    }


def test_load_expenses_tmp_path(tmp_path):
    file_path = tmp_path / "expenses.csv"
    file_path.write_text(
        "# date;category;amount;comment\n"
        "2026-09-21;food;100;lunch\n"
        "\n"
        "2026-09-22;transport;30;bus\n",
        encoding="utf-8"
    )

    records = load_expenses(file_path)

    assert len(records) == 2
    assert total_by_category(records) == {
        "food": 100.0,
        "transport": 30.0
    }


def test_real_expenses_file():
    records = load_expenses("data/expenses.csv")

    assert len(records) == 12
    assert total_by_category(records) == {
        "food": 590.0,
        "transport": 96.0,
        "coffee": 60.0,
        "entertainment": 230.0,
        "mobile": 100.0
    }