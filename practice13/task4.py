import math
import random
from pathlib import Path
from datetime import datetime

# Personal information
print("Sofia Stotska, IT-31")

# Birth year
YEAR = 2009

# Initialize random generator
random.seed(YEAR)

# Generate examples
number = random.randint(2, 20)
square = number ** 2

factorial_number = random.randint(3, 6)

a = random.randint(12, 99)
b = random.randint(12, 99)

n = random.randint(5, 10)
k = random.randint(2, n - 1)

percent = random.choice([5, 10, 15, 20, 25])
base = random.randint(5, 25) * 20

# Questions and answers
questions = [
    (f"sqrt({square})", math.isqrt(square)),
    (f"{factorial_number}!", math.factorial(factorial_number)),
    (f"gcd({a}, {b})", math.gcd(a, b)),
    (f"comb({n}, {k})", math.comb(n, k)),
    (f"{percent}% of {base}", percent * base // 100)
]

# Start timer
start_time = datetime.now()

score = 0

# Ask questions
for index, (question, correct_answer) in enumerate(questions, start=1):
    answer = input(f"{index}) {question} = ")

    try:
        user_answer = int(answer)
    except ValueError:
        user_answer = None

    if user_answer == correct_answer:
        print("   correct")
        score += 1
    else:
        print(f"   wrong, answer: {correct_answer}")

# Finish timer
end_time = datetime.now()
seconds = (end_time - start_time).total_seconds()

print(f"score: {score}/5, time: {seconds:.1f} s")

# History file
script_directory = Path(__file__).parent
results_directory = script_directory / "results"
results_directory.mkdir(exist_ok=True)

history_path = results_directory / "history.csv"

# Save attempt
attempt_time = end_time.strftime("%Y-%m-%d %H:%M")

if not history_path.exists():
    history_path.write_text(
        "# datetime;score;seconds\n",
        encoding="utf-8"
    )

with history_path.open("a", encoding="utf-8") as history:
    history.write(f"{attempt_time};{score};{seconds:.1f}\n")

# Read history
attempts = []

with history_path.open("r", encoding="utf-8") as history:
    for line in history:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        parts = line.split(";")

        try:
            attempt_date = datetime.strptime(
                parts[0], "%Y-%m-%d %H:%M"
            )
            attempt_score = int(parts[1])
            attempt_seconds = float(parts[2])

            attempts.append({
                "date": attempt_date,
                "score": attempt_score,
                "seconds": attempt_seconds
            })

        except (ValueError, IndexError):
            continue

# Find best result
best = max(
    attempts,
    key=lambda item: (item["score"], -item["seconds"])
)

print(
    f"attempts: {len(attempts)}, "
    f"best: {best['score']}/5 in "
    f"{best['seconds']:.1f} s "
    f"({best['date'].strftime('%Y-%m-%d %H:%M')})"
)