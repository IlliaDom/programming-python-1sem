# File: task4.py
from datetime import datetime
import math
from pathlib import Path
import random
import sys

print("Батура Каріна Віталіївна, ІТ-31")

random.seed(2009)

# Генеруємо параметри завдань
n_sqrt = random.choice([144, 196, 225, 256])
ans_sqrt = math.isqrt(n_sqrt)

n_fact = random.randint(3, 5)
ans_fact = math.factorial(n_fact)

n_gcd1, n_gcd2 = random.choice(
    [(48, 28), (36, 24), (54, 24), (60, 45)])
ans_gcd = math.gcd(n_gcd1, n_gcd2)

n_comb_n, n_comb_k = random.choice([(7, 2), (6, 2), (8, 3)])
ans_comb = math.comb(n_comb_n, n_comb_k)

pct_val = random.choice([5, 10, 20])
base_num = random.choice([200, 260, 300, 400])
ans_pct = (pct_val * base_num) // 100

questions = [
    (f"sqrt({n_sqrt})", ans_sqrt),
    (f"{n_fact}!", ans_fact),
    (f"gcd({n_gcd1}, {n_gcd2})", ans_gcd),
    (f"comb({n_comb_n}, {n_comb_k})", ans_comb),
    (f"{pct_val}% of {base_num}", ans_pct),
]

score = 0
start_time = datetime.now()

for i, (q_text, correct_ans) in enumerate(questions, 1):
    user_input = input(f"{i}) {q_text} = ").strip()
    try:
        user_val = int(user_input)
        if user_val == correct_ans:
            print("   correct")
            score += 1
        else:
            print(f"   wrong, answer: {correct_ans}")
    except ValueError:
        print(f"   wrong, answer: {correct_ans}")

end_time = datetime.now()
elapsed_seconds = round((end_time - start_time).total_seconds(), 1)

print(f"score: {score}/5, time: {elapsed_seconds} s")

# Робота з історією у results/history.csv
results_dir = Path("results")
results_dir.mkdir(exist_ok=True)
history_file = results_dir / "history.csv"

file_exists = history_file.exists()
with open(history_file, "a", encoding="utf-8") as f:
    if not file_exists:
        f.write("# datetime;score;seconds\n")
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    f.write(f"{now_str};{score};{elapsed_seconds}\n")

# Перечитуємо історію для статистики
attempts_count = 0
best_score = -1
best_time = float("inf")
best_dt = ""

with open(history_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(";")
        if len(parts) == 3:
            dt_s, sc_s, sec_s = parts
            sc = int(sc_s)
            sec = float(sec_s)
            attempts_count += 1
            if sc > best_score or (sc == best_score and sec < best_time):
                best_score = sc
                best_time = sec
                best_dt = dt_s

print(
    f"attempts: {attempts_count}, best: {best_score}/5 in {best_time} s ({best_dt})"
)