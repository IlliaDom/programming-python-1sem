from pathlib import Path

import pytest

from expenses import load_expenses, parse_line, total_by_category

REAL_FILE = Path(__file__).resolve().parent / "data" / "expenses.csv"

def test_parse_line_valid():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert record["category"] == "food"
    assert record["amount"] == 85.5


def test_parse_line_returns_all_fields():
    assert parse_line("2026-09-21;food;85.50;lunch") == {
        "date": "2026-09-21", "category": "food",
        "amount": 85.5, "comment": "lunch"}


def test_parse_line_amount_is_float():
    assert isinstance(parse_line("2026-09-21;food;85;lunch")["amount"], float)


def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;abc;lunch")


def test_parse_line_wrong_field_count():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50")

@pytest.mark.parametrize("line, category, amount", [
    ("2026-09-21;food;85.50;lunch", "food", 85.5),
    ("2026-09-21;transport;32.00;bus", "transport", 32.0),
    ("2026-09-22;food;14.50;coffee", "food", 14.5),
    ("2026-09-23;fun;265.00;cinema", "fun", 265.0),
    ("2026-09-24;food;128.50;dinner", "food", 128.5),
])
def test_parse_line_param(line, category, amount):
    record = parse_line(line)
    assert record["category"] == category
    assert record["amount"] == amount

def test_total_by_category(tmp_path):
    path = tmp_path / "expenses.csv"
    path.write_text(
        "# date;category;amount;comment\n"
        "2026-09-21;food;85.50;lunch\n"
        "\n"
        "2026-09-22;food;14.50;coffee\n",
        encoding="utf-8",
    )
    totals = total_by_category(load_expenses(path))
    assert totals == {"food": 100.0}

def test_total_by_category_real_file():
    expected = {"food": 150.5, "transport": 20.0}
    assert total_by_category(load_expenses(REAL_FILE)) == expected