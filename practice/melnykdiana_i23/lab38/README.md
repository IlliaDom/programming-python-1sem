# Практична робота П17 — готовий проєкт

**Студентка:** Мельник Діана, група І-23  
**Місто для запиту погоди:** Олика (50.72272, 25.81208)

## Запуск

У теці `lab38` створіть середовище та встановіть залежність:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```

Скопіюйте власний `data/expenses.csv` роботи 22 у цю теку замість наданої копії, якщо вона змінилася. Далі виконайте `python task1.py` … `python task5.py`.

Для завдання 4 запустіть окремо:

```bash
python task2.py --demo-error connection
python task2.py --demo-error http
python task2.py --demo-error timeout
```

Кожна помилкова демонстрація має надрукувати повідомлення в stderr і завершитися з кодом 1. Режим connection перевіряє з'єднання зі спеціально зарезервованою адресою, тому його тривалість залежить від мережі та системних налаштувань.

## Вміст

- `task1.py` — статус, Content-Type, кількість валют, USD та EUR.
- `task2.py` — підсумовує суми з `expenses.csv`, окремо отримує курси USD та EUR з НБУ та конвертує витрати.
- `task3.py` — поточна температура і вітер в Олиці через Open-Meteo.
- `task4` — три режими демонстрації помилок у `task2.py`.
- `task5.py` — кеш відповіді НБУ на одну годину у `cache/rates.json`.
- `report.pdf` — звіт і контрольні запитання.
