import pytest

from expenses import parse_line, load_expenses, total_by_category


def test_parse_line_valid():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert record["category"] == "food"
    assert record["amount"] == 85.5


def test_parse_line_all_fields():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert record == {"date": "2026-09-21", "category": "food", "amount": 85.5, "comment": "lunch"}


def test_parse_line_amount_is_float():
    record = parse_line("2026-09-22;transport;40;bus")
    assert isinstance(record["amount"], float)
    assert record["amount"] == 40.0


def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;abc;lunch")


def test_parse_line_wrong_fields_count():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50")


def test_parse_line_too_many_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50;lunch;extra")


@pytest.mark.parametrize("line, category, amount", [
    ("2026-09-21;food;85.50;lunch", "food", 85.5),
    ("2026-09-22;transport;40.00;bus", "transport", 40.0),
    ("2026-09-23;study;250.00;books", "study", 250.0),
    ("2026-09-24;food;14.50;coffee", "food", 14.5),
    ("2026-09-25;fun;120.00;cinema", "fun", 120.0),
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
    totals = total_by_category(load_expenses("data/expenses.csv"))
    assert totals == {"food": 100.0, "transport": 40.0, "study": 250.0, "fun": 120.0}
