from expenses import parse_line
def test_parse_line_valid():
    record = parse_line("2026-09-21|food|85.50|lunch")
    assert record["category"] == "food"
    assert record["amount"] == 85.5

import pytest
from pathlib import Path
def test_parse_line_bad_amount ():
    with pytest.raises(ValueError):
        parse_line("2026-09-21|food|bad_amount|lunch")
def test_parse_line_bad_length ():
    with pytest.raises(ValueError):
        parse_line("2026-09-21|food|230|lunch|damds")

with open(Path(__file__).resolve().parent / "data"/"expenses.csv" , "r", encoding="utf-8") as file:
    lines = file.readlines()[1:6]
@pytest.mark.parametrize("line", lines)
def test_parse_line(line):
    record = parse_line(line.strip())
    assert isinstance(record, dict)

from expenses import load_expenses, total_by_category

def test_total_by_category(tmp_path):
    path = tmp_path / "expenses.csv"
    path.write_text(
        "# date|category|amount|comment\n"
        "2026-09-21|food|85.50|lunch\n"
        "\n"
        "2026-09-22|food|14.50|coffee\n",
        encoding="utf-8",
    )
    totals = total_by_category(load_expenses(path))
    assert totals == {"food": 100.0}
from pathlib import Path


def test_total_by_category_real_file():
    path = Path(__file__).parent / "data" / "expenses.csv"

    totals = total_by_category(load_expenses(path))

    assert totals == {
        "Food": 2775.50,
        "Transport": 300.00,
        "Coffee": 480.00,
        "Entertainment": 1050.00,
        "Clothes": 1200.00,
        "Other": 640.00
    }