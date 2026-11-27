# Практична робота 22. Перевантаження операторів

Sofiia Zakharchuk, IT-32

## Завдання 1. Клас Money (task1.py)

```
Sofiia Zakharchuk, IT-32
float: False
Money: True
0.30 UAH
14.50 UAH
126.90 UAH | 126.90 UAH
Money(85.5, 'UAH')
True True False
error: different currencies: UAH and USD
```

Сума зберігається в копійках цілим числом, тому `Money(0.1) + Money(0.2) == Money(0.3)` дає `True`, а для `float` `0.1 + 0.2 == 0.3` дає `False`. Реалізовано `__add__`, `__sub__`, `__mul__` (і `__rmul__`, щоб працювало `3 * Money(...)`), `__eq__`, `__lt__` (решту порівнянь дописує `functools.total_ordering`), `__str__`, `__repr__` і `__hash__` (потрібен, бо після перевизначення `__eq__` об'єкти інакше не можна класти в множину). Додавання гривень і доларів викликає `ValueError`.

## Завдання 2. Сортування та сума (task2.py)

```
Sofiia Zakharchuk, IT-32
count: 14
--- sorted (works thanks to __lt__) ---
smallest 3: 16.00 UAH, 16.00 UAH, 16.00 UAH
biggest 3:  48.00 UAH, 52.00 UAH, 60.00 UAH
min: 16.00 UAH | max: 60.00 UAH
--- sum ---
sum(items, Money(0)): 510.00 UAH
sum(items):           510.00 UAH
sum([], Money(0)):    0.00 UAH
float sum of csv:     510.0
matches: True
--- Money(10) + 5 ---
without NotImplemented: AttributeError - 'int' object has no attribute 'cents'
with NotImplemented:    TypeError - unsupported operand type(s) for +: 'Money' and 'int'
```

- `sorted`, `min` і `max` працюють завдяки `__lt__`.
- `sum(items, Money(0))`: за замовчуванням `sum` починає з числа `0`, тобто першою виконується операція `0 + Money`. Тому в класі потрібен `__radd__`. Другий аргумент задає початкове значення `Money(0)`, і тоді додаються тільки `Money` з `Money`. До того ж для порожнього списку результат буде `0.00 UAH`, а не число `0`.
- Сума збігається з сумою тих самих значень з CSV (робота 22).
- `Money(10) + 5`: якщо в `__add__` одразу звертатися до `other.cents`, виникає незрозумілий `AttributeError`. Коли метод повертає `NotImplemented`, Python спробує `int.__radd__`, а потім сам генерує зрозумілий `TypeError`.

## Завдання 3. Колекція витрат (task3.py)

```
Sofiia Zakharchuk, IT-32
first half:  ExpenseBook: 0 expenses, total 0.00 UAH
second half: ExpenseBook: 14 expenses, total 510.00 UAH
merged:      ExpenseBook: 14 expenses, total 510.00 UAH
len check: 14 == 0 + 14 -> True
categories: coffee, food, snacks, stationery, transport
in: True | 'unicorn' in: False
book[0]: Expense(date=datetime.date(2026, 9, 21), category='coffee', money=Money(45.0, 'UAH'), comment='coffee before lecture')
book[-1]: Expense(date=datetime.date(2026, 9, 27), category='coffee', money=Money(45.0, 'UAH'), comment='coffee with friend')
book[1:3]: 2 items
--- first 3 by iteration ---
2026-09-21  coffee      45.00 UAH
2026-09-21  food        38.00 UAH
2026-09-21  transport   16.00 UAH
bool(empty book): False
error: unsupported operand type(s) for +: 'ExpenseBook' and 'int'
```

`ExpenseBook` реалізує `__len__`, `__contains__`, `__iter__`, `__getitem__` (працюють і індекси, і зрізи), `__add__` (повертає нову книгу, не змінюючи старих) та `__str__`. Об'єднана книга містить усі витрати, `len` дорівнює сумі довжин двох книг. Порожня книга вважається хибною, бо `bool` бере `__len__`.

## Завдання 4. Бюджет (task4.py)

```
Sofiia Zakharchuk, IT-32
ExpenseBook: 14 expenses, total 510.00 UAH
budget: 4500.00 UAH
book > budget: False
book <= budget: True
within budget, left: 3990.00 UAH
```

Той самий запуск з маленьким бюджетом (python3 task4.py 300):

```
Sofiia Zakharchuk, IT-32
ExpenseBook: 14 expenses, total 510.00 UAH
budget: 300.00 UAH
book > budget: True
book <= budget: False
over budget by 210.00 UAH
```

Клас `BudgetBook` успадковує `ExpenseBook` і порівнює загальну суму витрат з `Money` через `__eq__` та `__lt__` (решту дає `total_ordering`). Різниця між бюджетом і витратами обчислюється оператором `-`.

## Контрольні запитання

1. **Спеціальні методи** (dunder-методи) — методи з іменами виду `__add__`, `__len__`, `__str__`. Ми їх самі зазвичай не викликаємо: Python викликає їх, коли виконує оператор чи вбудовану функцію. `a + b` — це `a.__add__(b)`, `len(a)` — `a.__len__()`, `print(a)` — `a.__str__()`.
2. Числа з плаваючою крапкою неточно подаються у двійковій системі (`0.1 + 0.2 = 0.30000000000000004`), і похибки накопичуються. Ціле число копійок рахується точно, а сума до відображення лише ділиться на 100. Для грошей це критично, бо помилка в копійках вводить людей в оману.
3. `__str__` повертає зрозумілий текст для користувача (`print`, `str`, f-рядок). `__repr__` дає однозначний опис для програміста, бажано у вигляді коду створення об'єкта (`Money(85.5, 'UAH')`), і використовується в інтерактивному режимі та для елементів списку. Якщо є тільки `__repr__`, його використовує й `print`.
4. З `NotImplemented` метод каже «я не вмію працювати з таким типом». Тоді Python спробує віддзеркалений метод іншого об'єкта (`__radd__`), а якщо й він не вміє, сам згенерує зрозумілий `TypeError`. Виняток, згенерований у методі, зупиняє цей механізм і не дає іншому типу шансу обробити операцію.
5. Мінімум метод `__lt__`: `sorted`, `min` і `max` порівнюють елементи оператором `<`. Для повного набору порівнянь додають `__eq__` і декоратор `functools.total_ordering`.
