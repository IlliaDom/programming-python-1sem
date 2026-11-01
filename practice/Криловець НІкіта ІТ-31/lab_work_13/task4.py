import math
import random
from pathlib import Path
from datetime import datetime

name = "Nikita"
surname = "Krilovets"
group = "IT-31"
year = 2009

print(f"{name} {surname}, {group}")

random.seed(year)

questions = []

square_root_number = random.randint(2, 20) ** 2
questions.append((
    f"sqrt({square_root_number})",
    math.isqrt(square_root_number)
))

factorial_number = random.randint(3, 6)
questions.append((
    f"{factorial_number}!",
    math.factorial(factorial_number)
))

number1 = random.randint(20, 100)
number2 = random.randint(20, 100)
questions.append((
    f"gcd({number1}, {number2})",
    math.gcd(number1, number2)
))

comb_n = random.randint(5, 10)
comb_k = random.randint(2, comb_n - 2)
questions.append((
    f"comb({comb_n}, {comb_k})",
    math.comb(comb_n, comb_k)
))

percent = random.choice([5, 10, 20, 25, 50])
amount = random.randint(10, 100) * 20
questions.append((
    f"{percent}% of {amount}",
    percent * amount // 100
))

score = 0

start_time = datetime.now()

for i, (question, correct_answer) in enumerate(questions, start=1):
    answer = input(f"{i}) {question} = ")

    try:
        user_answer = int(answer.strip())

        if user_answer == correct_answer:
            print("   correct")
            score += 1
        else:
            print(f"   wrong, answer: {correct_answer}")

    except ValueError:
        print(f"   wrong, answer: {correct_answer}")

end_time = datetime.now()

elapsed = (end_time - start_time).total_seconds()

print(f"score: {score}/5, time: {elapsed:.1f} s")

results_dir = Path(__file__).parent / "results"
results_dir.mkdir(exist_ok=True)

history_file = results_dir / "history.csv"

if not history_file.exists():
    history_file.write_text(
        "# datetime;score;seconds\n",
        encoding="utf-8"
    )

attempt_time = end_time.strftime("%Y-%m-%d %H:%M")

with history_file.open("a", encoding="utf-8") as file:
    file.write(f"{attempt_time};{score};{elapsed:.1f}\n")

attempts = []

with history_file.open("r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        try:
            parts = line.split(";")

            attempt_date = datetime.strptime(
                parts[0], "%Y-%m-%d %H:%M"
            )

            attempt_score = int(parts[1])
            attempt_seconds = float(parts[2])

            attempts.append((
                attempt_date,
                attempt_score,
                attempt_seconds
            ))

        except (ValueError, IndexError):
            continue

best_attempt = min(
    attempts,
    key=lambda attempt: (-attempt[1], attempt[2])
)

best_date = best_attempt[0].strftime("%Y-%m-%d %H:%M")

print(
    f"attempts: {len(attempts)}, "
    f"best: {best_attempt[1]}/5 "
    f"in {best_attempt[2]:.1f} s ({best_date})"
)