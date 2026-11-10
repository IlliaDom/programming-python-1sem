print("Mushka Vlad IT31")

import random
import math
from datetime import datetime
from pathlib import Path

year = 2009
random.seed(year)

results = Path(__file__).parent / "results"
results.mkdir(exist_ok=True)

history = results / "history.csv"

a = random.randint(10, 20)
b = random.randint(2, 6)
c = random.randint(20, 50)
d = random.randint(10, 20)
e = random.randint(100, 500)

questions = [
    (f"sqrt({a * a})", math.isqrt(a * a)),
    (f"{b}!", math.factorial(b)),
    (f"gcd({c}, {d})", math.gcd(c, d)),
    (f"comb({a}, 2)", math.comb(a, 2)),
    (f"5% of {e}", 5 * e // 100)
]

score = 0
start = datetime.now()

for i, (question, correct_answer) in enumerate(questions, 1):
    answer = input(f"{i}) {question} = ")

    try:
        if int(answer) == correct_answer:
            print("   correct")
            score += 1
        else:
            print(f"   wrong, answer: {correct_answer}")
    except ValueError:
        print(f"   wrong, answer: {correct_answer}")

seconds = (datetime.now() - start).total_seconds()

print(f"score: {score}/5, time: {seconds:.1f} s")

if not history.exists():
    history.write_text("# datetime;score;seconds\n", encoding="utf-8")

with history.open("a", encoding="utf-8") as file:
    file.write(
        f"{datetime.now():%Y-%m-%d %H:%M};{score};{seconds:.1f}\n"
    )

attempts = []

with history.open("r", encoding="utf-8") as file:
    for line in file:
        if line.startswith("#") or not line.strip():
            continue

        date, points, time = line.strip().split(";")
        attempts.append((int(points), float(time), date))

best = max(attempts, key=lambda item: (item[0], -item[1]))

print(
    f"attempts: {len(attempts)}, "
    f"best: {best[0]}/5 in {best[1]:.1f} s ({best[2]})"
)