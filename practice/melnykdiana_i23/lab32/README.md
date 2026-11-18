# Практична робота 14 — зовнішні бібліотеки

**Студентка:** Diana Melnyk  
**Група:** I-23

## Структура
- `task2.py` — аналіз витрат із CSV за категоріями через `tabulate`.
- `task3.py` — створення QR-коду контактів.
- `data/expenses.csv` — персональні дані витрат із попередньої практичної.
- `contact.png` — згенерований QR-код.
- `requirements.txt` — зафіксовані залежності.
- `.gitignore` — виключає `.venv`.

## Запуск у Git Bash (Windows)
cd lab32
py -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
python task2.py
python task3.py

Для Linux/macOS активація: `source .venv/bin/activate`.

## Копія середовища
Створіть поруч `lab32_copy`, скопіюйте туди `task2.py`, `data/` та `requirements.txt`, а потім виконайте:
cd ../lab32_copy
py -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
python task2.py

Не додавайте `.venv/` до Git. Після виконання експерименту з видаленням `qrcode` для відновлення виконайте `python -m pip install -r requirements.txt`.
