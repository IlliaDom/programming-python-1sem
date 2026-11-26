from pathlib import Path

import pytest

from expenses import load_expenses, parse_line, total_by_category

DATA_FILE = Path(__file__).parent / "data" / "expenses.csv"


# ---------- Завдання 2: перші тести з assert ----------

def test_parse_line_valid():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert record["category"] == "food"
    assert record["amount"] == 85.5


def test_parse_line_returns_all_fields():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert record == {
        "date": "2026-09-21",
        "category": "food",
        "amount": 85.5,
        "comment": "lunch",
    }


def test_parse_line_amount_is_float():
    record = parse_line("2026-09-22;transport;40;metro")
    assert isinstance(record["amount"], float)


# ---------- Завдання 3: перевірка винятків ----------

def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;abc;lunch")


def test_parse_line_too_few_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50")


def test_parse_line_too_many_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50;lunch;extra")


# ---------- Завдання 4: параметризований тест ----------

# П'ять рядків з мого файлу витрат (data/expenses.csv)
@pytest.mark.parametrize(
    "line, category, amount",
    [
        ("2026-11-06;food;78.00;lunch at canteen", "food", 78.0),
        ("2026-11-07;coffee;55.00;before the lecture", "coffee", 55.0),
        ("2026-11-08;books;180.00;sql notebook", "books", 180.0),
        ("2026-11-10;internet;230.00;monthly plan", "internet", 230.0),
        ("2026-11-11;transport;28.00;bus to college", "transport", 28.0),
    ],
)
def test_parse_line_parametrized(line, category, amount):
    record = parse_line(line)
    assert record["category"] == category
    assert record["amount"] == amount


# ---------- Завдання 5: тимчасовий файл і справжній файл ----------

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
    # Очікувані суми пораховані вручну з data/expenses.csv:
    # food = 78 + 134.5 + 42 + 110 + 69.5 + 95 = 529.0
    # transport = 28 * 3 = 84.0; coffee = 55 + 55 + 60 = 170.0
    totals = total_by_category(load_expenses(DATA_FILE))
    assert totals == {
        "food": 529.0,
        "transport": 84.0,
        "coffee": 170.0,
        "books": 180.0,
        "internet": 230.0,
    }
    assert len(load_expenses(DATA_FILE)) == 14
