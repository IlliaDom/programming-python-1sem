import random
import math 
from datetime import datetime
from pathlib import Path

print("Студент: Богдана Цихович, група: ІТ-32")

year = 2007 
random.seed(year)

questions = []

n = random.randint(1, 20)
questions.append((f"sqrt({n**2})", math.isqrt(n**2)))

n = random.randint(1, 10)
questions.append((f"{n}!", math.factorial(n)))

n = random.randint(1, 50)
m = random.randint(1, 50)
questions.append((f"gcd({n}, {m})", math.gcd(n, m)))

n = random.randint(1, 10)
k = random.randint(1, 10)
questions.append((f"comb({n}, {k})", math.comb(n, k)))

percent = random.choice([5, 10, 15, 20])
number = random.randrange(100, 1000, 10)
questions.append((f"{percent}% of {number}", number * percent // 100))

start = datetime.now()
score = 0

for i, (question, answer) in enumerate(questions, 1):
    user_answer = input(f"Приклад {i}: {question} = ")
    try:
        user_answer = int(user_answer)
        if user_answer == answer:
            print("Правильно!")
            score += 1
        else:
            print(f"Неправильно. Правильна відповідь: {answer}")
    except ValueError:
        print(f"Неправильний формат відповіді. Правильна відповідь: {answer}")

end = datetime.now()
seconds = (end - start).total_seconds()

print(f"Результат: {score}/5")
print(f"Час: {seconds:.2f} секунд")

results_file = Path(__file__).parent / "results" 
results_file.mkdir(exist_ok=True)

history = results_file / "history.csv"

if not history.exists():
    with open(history, 'w', encoding='utf-8') as f:
        f.write("# datetime;score;seconds\n")

with open(history, 'a', encoding='utf-8') as f:
    f.write(f"{end.strftime('%Y-%m-%d %H:%M:%S')};{score};{seconds:.2f}\n")

attempts = []
with open(history, 'r', encoding='utf-8') as f:
    next(f)
    for line in f:
        dt, s, sec = line.strip().split(';')
        attempts.append((int(s), float(sec), dt))

    def get_best(item):
        return (item[0], -item[1])  
    best_score = max(attempts, key=get_best)

print(f"Кількість спроб: {len(attempts)}")
print(f"Найкращий результат: {best_score[0]}/5 за {best_score[1]:.2f} секунд")
print(f"Дата: {best_score[2]}")
