
import random
import math
import csv
from pathlib import Path
from datetime import datetime

# Рік народження — 2008
random.seed(2008)

HISTORY = Path(__file__).parent / "results" / "history.csv"


def generate_questions():
    questions = []

    a = random.randint(2, 12)
    questions.append((f"Знайдіть квадратний корінь із {a * a}", math.isqrt(a * a)))

    n = random.randint(3, 6)
    questions.append((f"Знайдіть факторіал числа {n}", math.factorial(n)))

    a = random.randint(10, 50)
    b = random.randint(5, 30)
    questions.append((f"Знайдіть НСД чисел {a} і {b}", math.gcd(a, b)))

    n = random.randint(5, 10)
    k = random.randint(2, n - 2)
    questions.append((f"Обчисліть кількість комбінацій C({n}, {k})", math.comb(n, k)))

    amount = random.randint(100, 1000)
    questions.append((f"Скільки становить 5% від {amount}?", amount * 5 // 100))

    return questions


def save_result(score, seconds):
    HISTORY.parent.mkdir(parents=True, exist_ok=True)

    new_file = not HISTORY.exists()

    with HISTORY.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")

        if new_file:
            file.write("# datetime;score;seconds\n")

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            score,
            f"{seconds:.2f}"
        ])


def show_history():
    print("\nІсторія результатів:")

    if not HISTORY.exists():
        print("Історія поки порожня.")
        return

    results = []

    with HISTORY.open("r", encoding="utf-8") as file:
        for row in csv.reader(file, delimiter=";"):
            if not row or row[0].startswith("#"):
                continue

            results.append((int(row[1]), float(row[2])))

    if not results:
        print("Історія поки порожня.")
        return

    best = min(results, key=lambda item: (-item[0], item[1]))

    print(f"Кількість спроб: {len(results)}")
    print(f"Найкращий результат: {best[0]}/5 за {best[1]:.2f} сек.")


def main():
    print("Diana Melnyk, група I-23")
    print("\nМатематичний тренажер")
    print("Введіть відповіді на 5 запитань.\n")

    questions = generate_questions()
    score = 0

    start = datetime.now()

    for number, (question, correct) in enumerate(questions, start=1):
        print(f"{number}. {question}")

        answer = input("Ваша відповідь: ").strip()

        try:
            if answer and int(answer) == correct:
                print("Правильно!\n")
                score += 1
            else:
                print(f"Неправильно. Правильна відповідь: {correct}\n")
        except ValueError:
            print(f"Некоректне введення. Правильна відповідь: {correct}\n")

    end = datetime.now()
    seconds = (end - start).total_seconds()

    print(f"Ваш результат: {score}/5")
    print(f"Витрачений час: {seconds:.2f} сек.")

    save_result(score, seconds)
    show_history()


if __name__ == "__main__":
    main()
