Практична робота №36 — Серіалізація даних: JSON
Виконала: Вовк Марія Віталіївна, група І-23

Структура:
task1.py ... task4.py
data/expenses.csv
data/expenses.json
data/expenses_updated.json
settings.json
date_example.json
Звіт_П36_Вовк_Марія_І-23.pdf

Запуск у PowerShell з каталогу lab36:
python task1.py
python task2.py
python task3.py
python task4.py

Перевірка JSON:
python -m json.tool data/expenses.json

Для перевірки помилки task3:
1. Відкрийте settings.json.
2. Тимчасово видаліть кому після значення owner.
3. Запустіть python task3.py — програма покаже номер рядка помилки та завершиться з кодом 1.
4. Поверніть кому, щоб відновити коректний settings.json.
