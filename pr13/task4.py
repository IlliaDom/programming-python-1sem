import csv
import math
import random
from datetime import datetime
from pathlib import Path

NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"
YEAR = 2008

HISTORY = Path(__file__).resolve().parent / "results" / "history.csv"
HEADER = "# datetime;score;seconds"


def make_questions():
    random.seed(YEAR)
    root = random.randint(5, 20)
    n = random.randint(3, 8)
    a = random.randint(2, 12) * random.randint(2, 6)
    b = random.randint(2, 12) * random.randint(2, 6)
    total = random.randint(5, 10)
    k = random.randint(2, 4)
    num = random.randint(5, 30) * 10
    percent = random.choice([5, 10, 15, 20, 25])
    return [
        (f"sqrt({root * root})", math.isqrt(root * root)),
        (f"{n}!", math.factorial(n)),
        (f"gcd({a}, {b})", math.gcd(a, b)),
        (f"comb({total}, {k})", math.comb(total, k)),
        (f"{percent}% of {num}", num * percent // 100),
    ]


def read_history():
    attempts = []
    if not HISTORY.exists():
        return attempts
    with HISTORY.open(encoding="utf-8", newline="") as f:
        for row in csv.reader(f, delimiter=";"):
            if not row or row[0].startswith("#"):
                continue
            try:
                when = datetime.strptime(row[0], "%Y-%m-%d %H:%M")
                attempts.append((when, int(row[1]), float(row[2])))
            except (ValueError, IndexError):
                continue
    return attempts


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    questions = make_questions()
    score = 0
    started = datetime.now()
    for i, (text, answer) in enumerate(questions, start=1):
        raw = input(f"{i}) {text} = ").strip()
        try:
            ok = int(raw) == answer
        except ValueError:
            ok = False
        if ok:
            score += 1
            print("   correct")
        else:
            print(f"   wrong, answer: {answer}")
    seconds = (datetime.now() - started).total_seconds()
    print(f"score: {score}/{len(questions)}, time: {seconds:.1f} s")

    HISTORY.parent.mkdir(exist_ok=True)
    new_file = not HISTORY.exists()
    with HISTORY.open("a", encoding="utf-8") as f:
        if new_file:
            f.write(HEADER + "\n")
        f.write(f"{started:%Y-%m-%d %H:%M};{score};{seconds:.1f}\n")

    attempts = read_history()
    best = min(attempts, key=lambda a: (-a[1], a[2]))
    print(f"attempts: {len(attempts)}, best: {best[1]}/{len(questions)} "
          f"in {best[2]:.1f} s ({best[0]:%Y-%m-%d %H:%M})")


if __name__ == "__main__":
    main()
