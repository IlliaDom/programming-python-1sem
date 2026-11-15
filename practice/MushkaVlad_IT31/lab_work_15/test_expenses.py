from pathlib import Path

import pytest

from expenses import parse_line


def test_parse_line_valid():
    record = parse_line("2026-09-21;food;85.50;lunch")

    assert record["category"] == "food"
    assert record["amount"] == 85.5
    assert record["comment"] == "lunch"


def test_parse_line_zero_amount():
    record = parse_line("2026-10-01;nothing;0.00;breakfast")

    assert record["amount"] == 0.0


def test_parse_line_decimal_amount():
    record = parse_line("2026-10-02;energy_drink;38.00;breakfast")

    assert record["category"] == "energy_drink"
    assert record["amount"] == 38.0
def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;abc;lunch")


def test_parse_line_wrong_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50")
@pytest.mark.parametrize(
    "line, expected_category, expected_amount",
    [
        ("2026-09-30;transfer;35.00;dinner", "transfer", 35.0),
        ("2026-09-30;nothing;0.00;breakfast", "nothing", 0.0),
        ("2026-09-30;water;35.00;lunch", "water", 35.0),
        ("2026-09-30;transfer;200.00;dinner", "transfer", 200.0),
        ("2026-10-02;energy_drink;38.00;breakfast", "energy_drink", 38.0),
    ],
)
def test_parse_line_parametrized(line, expected_category, expected_amount):
    record = parse_line(line)

    assert record["category"] == expected_category
    assert record["amount"] == expected_amount
from expenses import load_expenses, total_by_category


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
    path = Path(__file__).parent / "data" / "expenses.csv"

    records = load_expenses(path)
    totals = total_by_category(records)

    assert totals == {
        "transfer": 235.0,
        "nothing": 0.0,
        "water": 70.0,
        "energy_drink": 38.0,
    }