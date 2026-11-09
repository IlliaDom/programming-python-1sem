import math
import random
import sys
from pathlib import Path
from datetime import datetime

NAME_SURNAME = "Oleksandra Romanich"
GROUP = "IT-32"
YEAR = 2007

def main():
    print(f"{NAME_SURNAME}, {GROUP}")
    
    random.seed(YEAR)

    tasks = []
    
    a = random.randint(10, 20)
    tasks.append((f"sqrt({a*a})", math.isqrt(a*a)))
    
    b = random.randint(3, 6)
    tasks.append((f"{b}!", math.factorial(b)))
    
    c, d = random.randint(20, 50), random.randint(10, 30)
    tasks.append((f"gcd({c}, {d})", math.gcd(c, d)))
    
    e, f = random.randint(5, 10), random.randint(2, 4)
    tasks.append((f"comb({e}, {f})", math.comb(e, f)))
    
    g, h = random.randint(100, 300), random.randint(2, 10)
    tasks.append((f"{h}% of {g}", (g * h) // 100))

    start_time = datetime.now()
    score = 0

    for i, (question, correct_answer) in enumerate(tasks, 1):
        print(f"{i}) {question} = ", end="")
        try:
            user_input = input().strip()
            if user_input.isdigit() or (user_input.startswith("-") and user_input[1:].isdigit()):
                user_answer = int(user_input)
                if user_answer == correct_answer:
                    print("   correct")
                    score += 1
                else:
                    print(f"   wrong, answer: {correct_answer}")
            else:
                print(f"   wrong, answer: {correct_answer}")
        except (KeyboardInterrupt, EOFError):
            print("\nInterrupted.")
            sys.exit(1)

    end_time = datetime.now()
    elapsed = (end_time - start_time).total_seconds()

    print(f"score: {score}/5, time: {elapsed:.1f} s")

    results_dir = Path(__file__).parent / "results"
    results_dir.mkdir(exist_ok=True)
    history_file = results_dir / "history.csv"

    if not history_file.exists():
        with history_file.open("w", encoding="utf-8") as f:
            f.write("# datetime;score;seconds\n")

    with history_file.open("a", encoding="utf-8") as f:
        f.write(f"{end_time.strftime('%Y-%m-%d %H:%M')};{score};{elapsed:.1f}\n")

    attempts = 0
    best_score = -1
    best_time = float('inf')
    best_date = ""

    with history_file.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(";")
            if len(parts) == 3:
                attempts += 1
                dt_str, sc, tm = parts
                sc, tm = int(sc), float(tm)
                if sc > best_score or (sc == best_score and tm < best_time):
                    best_score = sc
                    best_time = tm
                    best_date = dt_str

    print(f"attempts: {attempts}, best: {best_score}/5 in {best_time:.1f} s ({best_date})")

if __name__ == "__main__":
    main()