
import csv
import math
import random
from pathlib import Path
from datetime import datetime

random.seed(2009)

print("Ira Leshchuk, IT-31")
print("МАТЕМАТИЧНА ВІКТОРИНА")

questions = [
    ("Скільки буде 12 у квадраті?", lambda: 12 ** 2, 144),
    ("Який факторіал числа 5?", lambda: math.factorial(5), 120),
    ("Найбільший спільний дільник 48 і 18?", lambda: math.gcd(48, 18), 6),
    ("Скільки буде 10 вибрати 2?", lambda: math.comb(10, 2), 45),
    ("Скільки буде 25% від 200?", lambda: 200 * 25 // 100, 50),
]

random.shuffle(questions)

score = 0
start_time = datetime.now()

for number, (question, calculate, correct_answer) in enumerate(questions, 1):
    print(f"\nПитання {number}: {question}")
    answer = input("Ваша відповідь: ")

    if answer.isdigit() and int(answer) == calculate():
        print("Правильно!")
        score += 1
    else:
        print(f"Неправильно. Правильна відповідь: {correct_answer}")

end_time = datetime.now()
elapsed = (end_time - start_time).total_seconds()

print("\nРЕЗУЛЬТАТИ")
print(f"Правильних відповідей: {score} з 5")
print(f"Час виконання: {elapsed:.2f} секунд")

results_folder = Path("results")
results_folder.mkdir(exist_ok=True)

history_file = results_folder / "history.csv"
file_exists = history_file.exists()

with history_file.open("a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")

    if not file_exists:
        writer.writerow(["Дата", "Бали", "Час"])

    writer.writerow([
        datetime.now().strftime("%d.%m.%Y %H:%M"),
        score,
        round(elapsed, 2)
    ])

print("\nІСТОРІЯ РЕЗУЛЬТАТІВ")

with history_file.open("r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")
    history = list(reader)

for item in history:
    print(f"{item['Дата']} | {item['Бали']} балів | {item['Час']} сек.")

best_score = max(int(item["Бали"]) for item in history)
fastest = min(float(item["Час"]) for item in history)

print(f"\nНайкращий результат: {best_score} балів")
print(f"Найшвидший час: {fastest} секунд")
print("\nВікторину завершено!")
