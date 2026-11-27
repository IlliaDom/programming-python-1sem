# Практична 20: Наслідування та перевизначення методів

Sofiia Zakharchuk, IT-32

## Завдання 1

```
Sofiia Zakharchuk, IT-32
Богдана Цихович, IT-32, group leader, +380 67 000 00 00
```

## Завдання 2

```

isinstance(object, Class)
object               Person      Student  GroupLeader
person                 True        False        False
student                True         True        False
leader                 True         True         True

issubclass(Class, Class)
class                Person      Student  GroupLeader
Person                 True        False        False
Student                True         True        False
GroupLeader            True         True         True

GroupLeader.__mro__:
['GroupLeader', 'Student', 'Person', 'object']
Богдана Цихович, IT-32, group leader, +380 67 000 00 00
```

## Завдання 3

```
monthly costs:
  stationery   Expense                35.00
  transport    RecurringExpense      352.00
  coffee       RecurringExpense      360.00
  rent         SharedExpense        3000.00
  internet     SharedExpense         100.00
total: 3847.00
```

## Завдання 4

```
before:
  stationery   Expense                35.00
  transport    RecurringExpense      352.00
  coffee       RecurringExpense      360.00
  rent         SharedExpense        3000.00
  internet     SharedExpense         100.00
total: 3847.00
after adding YearlyExpense:
  stationery   Expense                35.00
  transport    RecurringExpense      352.00
  coffee       RecurringExpense      360.00
  rent         SharedExpense        3000.00
  internet     SharedExpense         100.00
  subscription YearlyExpense         100.00
total: 3947.00
```

## Пояснення до завдання 2

`GroupLeader.__mro__` показує порядок пошуку: `GroupLeader → Student → Person → object`. Виклик `leader.describe()` бере метод із `GroupLeader`; його `super().describe()` переходить до `Student`, а той через `super()` — до `Person`. Тому опис збирається з усіх рівнів. `isinstance(leader, Person)` повертає `True`, бо `GroupLeader` є нащадком `Person` (через `Student`), а `isinstance` враховує наслідування. Зворотне неправильне: `isinstance(person, Student)` — `False`, бо батько не знає про нащадків.

## Контрольні запитання

1. **Що таке наслідування і навіщо воно потрібне?** Механізм, за яким клас-нащадок отримує атрибути й методи батьківського класу та може додавати власні або змінювати успадковані (відношення «є різновидом»). Потрібне, щоб не дублювати код: спільне лежить в одному місці.
2. **Навіщо викликати `super().__init__()` у конструкторі нащадка?** Конструктор батька автоматично не викликається, якщо в нащадка є власний `__init__`. Без виклику атрибути батька (`name`, `surname`) не створяться, і виникне `AttributeError`.
3. **Що таке перевизначення методу?** Оголошення в нащадку методу з тим самим іменем, що й у батька; для об'єктів нащадка викликається нова версія. За потреби батьківську версію викликають через `super()`.
4. **Що показує `__mro__`?** Порядок, у якому Python шукає атрибути й методи: від класу об'єкта вгору по ієрархії до `object`. `super()` викликає метод наступного класу в цьому списку.
5. **Чому в завданні 3 не потрібно перевіряти тип об'єкта в циклі?** Кожен клас сам реалізує `monthly_cost()` по-своєму, тому цикл просто викликає цей метод, а потрібна версія обирається автоматично. Це дозволило додати `YearlyExpense` без змін циклу (поліморфізм).
