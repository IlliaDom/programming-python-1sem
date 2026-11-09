def read_grade(prompt: str) -> int:
    while True:
        try:
            grade = input(prompt)
            grade_int = int(grade)
            if 0 <= grade_int <= 100:
                return grade_int
            else:
                print("Error: the value must be between 0 and 100")
        except ValueError:
            print("Error: digits only")
def to_letter(grade: int) -> str:
    if grade >= 90:
        return "A"
    if grade >= 80:
        return "B"
    if grade >= 70:
        return "C"
    if grade >= 60:
        return "D"
    if grade >= 50:
        return "E"
    return "F"
def average(grades: list) -> float:
    if not grades:
        return 0.0
    return sum(grades) / len(grades)
def count_above(grades: list, limit: float) -> int:
    count = 0
    for grade in grades:
        if grade > limit:
            count += 1
    return count
def print_report(name: str, group: str, grades: list) -> None:
    avg = average(grades)
    letter = to_letter(avg)
    best = max(grades) if grades else 0
    worst = min(grades) if grades else 0
    above_avg = count_above(grades, avg)
    
    print("--- Report ---")
    print(f"Student: {name}, group {group}")
    print(f"Grades: {' '.join(str(g) for g in grades)}")
    print(f"Average: {avg:.2f} -> {letter}")
    print(f"Best: {best}, worst: {worst}")
    print(f"Above average: {above_avg}")
def main() -> None:
    name = "Sasha"
    group = "IT-32"
    n = max(3, len(name))
    
    grades = []
    for i in range(n):
        prompt = f"Grade {i+1} (0-100): "
        grade = read_grade(prompt)
        grades.append(grade)
    
    print_report(name, group, grades)
if __name__ == "__main__":
    main()