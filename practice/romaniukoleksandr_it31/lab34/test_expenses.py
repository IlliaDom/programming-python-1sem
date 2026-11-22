import pytest

from expenses import parse_line, load_expenses, total_by_category

def test_parse_line_valid():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert record["category"] == "food"
    assert record["amount"] == 85.5

    assert record["date"] == "2026-09-21"
    assert record["comment"] == "lunch"
    

def test_parse_line_type():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert type(record) == type({})


def test_parse_line_tabulation():
    record = parse_line("2026-09-21;food;85.50;lunch\n")
    assert record["comment"] != "lunch\n"


def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;fifty;lunch")


def test_parse_line_bad_length():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50")


@pytest.mark.parametrize(
    ("line", "expected_category", "expected_amount"), 
    [
        ("2026-10-07;books;700.00;Hobit", "books", 700.00),
        ("2026-10-07;transport;24.00;Trolleybus", "transport", 24.00),
        ("2026-10-10;food;20.00;Bread", "food", 20.00),
        ("2026-10-12;food;124.00;Cookies", "food", 124.00),
        ("2026-10-16;books;1224.00;Lord of the rings", "books", 1224.00),
    ],
)
def test_parse_line(line, expected_category, expected_amount):
    assert parse_line(line)["category"] == expected_category
    assert parse_line(line)["amount"] == expected_amount


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


def test_total_by_category_real():
    path = "data/expenses.csv"
        
    totals = total_by_category(load_expenses(path))
    assert totals == {"books": 1924.0, "transport": 192.0, "food": 164.0}