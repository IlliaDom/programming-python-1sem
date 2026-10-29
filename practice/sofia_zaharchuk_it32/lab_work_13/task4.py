import math
import random
from datetime import datetime
from pathlib import Path

NAME, SURNAME, GROUP = "Sofiia", "Zakharchuk", "IT-32"
YEAR = 2008

HISTORY = Path(__file__).resolve().parent / "results" / "history.csv"


def make_questions() -> list[tuple[str, int]]:
    random.seed(YEAR)
    r = random.randint(5, 20)
    n = random.randint(3, 7)
    a, b = random.randint(10, 60), random.randint(10, 60)
    cn, ck = random.randint(5, 9), random.randint(2, 3)
    pct, base = random.choice([5, 10, 15, 20, 25]), random.randrange(100, 500, 20)
    return [
        (f"sqrt({r * r})", math.isqrt(r * r)),
        (f"{n}!", math.factorial(n)),
        (f"gcd({a}, {b})", math.gcd(a, b)),
        (f"comb({cn}, {ck})", math.comb(cn, ck)),
        (f"{pct}% of {base}", pct * base // 100),
    ]


def read_history() -> list[tuple[str, int, float]]:
    rows = []
    for line in HISTORY.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        dt, score, sec = line.split(";")
        rows.append((dt, int(score), float(sec)))
    return rows


def main() -> None:
    print(f"{NAME} {SURNAME}, {GROUP}")
    questions = make_questions()
    score = 0
    start = datetime.now()
    for i, (text, answer) in enumerate(questions, 1):
        try:
            given = int(input(f"{i}) {text} = ").strip())
        except (ValueError, EOFError):
            given = None
        if given == answer:
            score += 1
            print("   correct")
        else:
            print(f"   wrong, answer: {answer}")
    seconds = (datetime.now() - start).total_seconds()
    print(f"score: {score}/{len(questions)}, time: {seconds:.1f} s")

    HISTORY.parent.mkdir(exist_ok=True)
    new = not HISTORY.exists()
    with open(HISTORY, "a", encoding="utf-8") as f:
        if new:
            f.write("# datetime;score;seconds\n")
        f.write(f"{start:%Y-%m-%d %H:%M};{score};{seconds:.1f}\n")

    rows = read_history()
    best = max(rows, key=lambda r: (r[1], -r[2]))
    print(f"attempts: {len(rows)}, best: {best[1]}/{len(questions)} in {best[2]:.1f} s ({best[0]})")


main()
