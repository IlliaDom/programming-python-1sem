import math
import random
import sys
from datetime import datetime
from pathlib import Path

name, surname, group = "Yaroslav", "Korolchuk", "IT-31"
YEAR = 2007  # постав свій рік народження

print(f"{name} {surname}, {group}")

random.seed(YEAR)
r = random.randint(5, 20)
f = random.randint(3, 7)
a = random.randint(10, 99)
b = random.randint(10, 99)
n = random.randint(5, 12)
k = random.randint(2, 4)
p = random.choice([5, 10, 15, 20, 25])
x = random.randrange(100, 501, 20)

tasks = [
    (f"sqrt({r * r})", math.isqrt(r * r)),
    (f"{f}!", math.factorial(f)),
    (f"gcd({a}, {b})", math.gcd(a, b)),
    (f"comb({n}, {k})", math.comb(n, k)),
    (f"{p}% of {x}", x * p // 100),
]

score = 0
start = datetime.now()
for i, (text, answer) in enumerate(tasks, 1):
    user = input(f"{i}) {text} = ")
    try:
        ok = int(user.strip()) == answer
    except ValueError:
        ok = False
    if ok:
        print("   correct")
        score += 1
    else:
        print(f"   wrong, answer: {answer}")
seconds = (datetime.now() - start).total_seconds()
print(f"score: {score}/5, time: {seconds:.1f} s")

path = Path(__file__).parent / "results" / "history.csv"
path.parent.mkdir(exist_ok=True)
if not path.exists():
    path.write_text("# datetime;score;seconds\n", encoding="utf-8")
with path.open("a", encoding="utf-8") as fh:
    fh.write(f"{start:%Y-%m-%d %H:%M};{score};{seconds:.1f}\n")

rows = []
with path.open(encoding="utf-8") as fh:
    for num, line in enumerate(fh, 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            d, s, t = line.split(";")
            rows.append((d, int(s), float(t)))
        except ValueError:
            print(f"warning: line {num} skipped", file=sys.stderr)

best = max(rows, key=lambda row: (row[1], -row[2]))
print(f"attempts: {len(rows)}, best: {best[1]}/5 in {best[2]} s ({best[0]})")