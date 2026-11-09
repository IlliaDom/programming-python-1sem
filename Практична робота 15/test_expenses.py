import pytest

from expenses import load_expenses, parse_line, total_by_category


def test_parse_line_valid():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert record["date"] == "2026-09-21"
    assert record["category"] == "food"
    assert record["amount"] == 85.5
    assert record["comment"] == "lunch"


def test_parse_line_returns_float():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert isinstance(record["amount"], float)


def test_parse_line_no_extra_whitespace():
    record = parse_line("  2026-09-21;food;85.50;lunch  \n")
    assert record["category"] == "food"
    assert record["amount"] == 85.5


def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;abc;lunch")


def test_parse_line_too_few_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50")


def test_parse_line_too_many_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50;lunch;extra")


@pytest.mark.parametrize(
    "line, expected_category, expected_amount",
    [
        ("2026-09-21;food;85.50;lunch",            "food",          85.50),
        ("2026-09-22;food;14.50;coffee",           "food",          14.50),
        ("2026-09-23;transport;30.00;metro",       "transport",     30.00),
        ("2026-09-24;entertainment;120.00;cinema", "entertainment", 120.00),
        ("2026-09-25;utilities;450.75;internet",   "utilities",     450.75),
    ],
)
def test_parse_line_parametrized(line, expected_category, expected_amount):
    record = parse_line(line)
    assert record["category"] == expected_category
    assert record["amount"] == expected_amount


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


def test_load_expenses_skips_comments_and_blank_lines(tmp_path):
    path = tmp_path / "expenses.csv"
    path.write_text(
        "# header\n"
        "2026-09-21;food;10.00;a\n"
        "\n"
        "   \n"
        "2026-09-22;transport;5.50;b\n",
        encoding="utf-8",
    )
    records = load_expenses(path)
    assert len(records) == 2
    assert records[0]["category"] == "food"
    assert records[1]["amount"] == 5.5


def test_total_by_category_real_file():
    records = load_expenses("data/expenses.csv")
    totals = total_by_category(records)

    expected = {
        "food": 100.0,
        "transport": 30.0,
        "entertainment": 120.0,
    }
    assert totals == expected