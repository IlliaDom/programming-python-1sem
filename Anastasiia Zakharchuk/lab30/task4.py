import math
import random
from datetime import datetime
from pathlib import Path

NAME = "Anastasia"
SURNAME = "Zakharchuk"
GROUP = "IT-32"
YEAR = 2008

BASE = Path(__file__).resolve().parent
RESULTS_DIR = BASE / "results"
HISTORY = RESULTS_DIR / "history.csv"


def make_questions():
    n = random.choice([49, 81, 121, 144, 169, 196, 225])
    f = random.randint(3, 6)
    a = random.randint(12, 60)
    b = random.randint(6, 30)
    k = random.randint(5, 9)
    r = random.randint(2, 4)
    p = random.choice([5, 10, 15, 20])
    base = random.randint(10, 50) * 10
    return [
        (f"sqrt({n})", math.isqrt(n)),
        (f"{f}!", math.factorial(f)),
        (f"gcd({a}, {b})", math.gcd(a, b)),
        (f"comb({k}, {r})", math.comb(k, r)),
        (f"{p}% of {base}", base * p // 100),
    ]


def read_history():
    attempts = []
    if not HISTORY.exists():
        return attempts
    with open(HISTORY, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            stamp, score, seconds = line.split(";")
            attempts.append((stamp, int(score), float(seconds)))
    return attempts


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    random.seed(YEAR)
    questions = make_questions()

    start = datetime.now()
    score = 0
    for number, (text, answer) in enumerate(questions, start=1):
        reply = input(f"{number}) {text} = ")
        try:
            correct = int(reply) == answer
        except ValueError:
            correct = False
        if correct:
            print("   correct")
            score += 1
        else:
            print(f"   wrong, answer: {answer}")
    seconds = (datetime.now() - start).total_seconds()

    print(f"score: {score}/{len(questions)}, time: {seconds:.1f} s")

    RESULTS_DIR.mkdir(exist_ok=True)
    if not HISTORY.exists():
        HISTORY.write_text("# datetime;score;seconds\n", encoding="utf-8")
    stamp = start.strftime("%Y-%m-%d %H:%M")
    with open(HISTORY, "a", encoding="utf-8") as f:
        f.write(f"{stamp};{score};{seconds:.1f}\n")

    attempts = read_history()
    best = min(attempts, key=lambda a: (-a[1], a[2]))
    print(f"attempts: {len(attempts)}, best: {best[1]}/{len(questions)} "
          f"in {best[2]:.1f} s ({best[0]})")


main()