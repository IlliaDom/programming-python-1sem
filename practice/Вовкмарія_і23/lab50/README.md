# Практична робота №50 (П23)

Виконала: Вовк Марія Віталіївна, група І-23.

## Файли
- `expense.py` — клас Expense для записів витрат.
- `data/expenses.csv` — персональні витрати з практичної роботи 22.
- `data_loader.py` — завантаження витрат.
- `exporters.py` — абстрактний клас Exporter та експортери CSV, JSON і TXT.
- `task1.py` — перевірка абстрактного класу.
- `task2.py` — експорт у три формати.
- `task3.py` — незавершений експортер та HTML-експорт.
- `task4.py` — вибір формату з командного рядка.
- `report.csv`, `report.json`, `report.txt`, `report.html`, `user_report.json` — результати експорту.
- `report_50.pdf` — звіт із результатами та відповідями на контрольні запитання.

## Запуск
У каталозі `lab50`:
```powershell
python task1.py
python task2.py
python task3.py
python task4.py json
python task4.py csv
python task4.py txt
```
Для перевірки невідомого формату:
```powershell
python task4.py xml
```
Програма завершується з кодом 2.
