name = "Sasha"
surname = "Petrenko"
group = "IT-32"

def build_subjects():
    return [
        ("Programming", 3, 11),
        ("Math", 2, 8),
        ("English", 2, 10),
        ("Physics", 1, 6),
    ]

def print_table(subjects):
    print(f"{name} {surname}, {group}")
    print("#  Subject        Pairs  Grade")
    for i, (title, pairs, grade) in enumerate(subjects, start=1):
        print(f"{i}  {title:<14} {pairs:>4}  {grade:>6}")

def total_pairs(subjects):
    return sum(p for _, p, _ in subjects)

def most_pairs(subjects):
    return max(subjects, key=lambda s: s[1])

def weakest(subjects):
    return min(subjects, key=lambda s: s[2])

def titles_list(subjects):
    return [t for t, _, _ in subjects]

def grades_list(subjects):
    return [g for _, _, g in subjects]

def average_grade(subjects):
    g = grades_list(subjects)
    return sum(g) / len(g) if g else 0.0

def grade_10_plus(subjects):
    return [t for t, _, g in subjects if g >= 10]

def print_histograms(subjects):
    for title, _, grade in subjects:
        print(f"{title}: {'#' * grade}")

def retake_lowest(subjects):
    low = weakest(subjects)
    new_grade = min(low[2] + 2, 12)
    print(f"Retake: {low[0]} {low[2]} -> {new_grade}")
    new_subjects = []
    for title, pairs, grade in subjects:
        if title == low[0]:
            new_subjects.append((title, pairs, new_grade))
        else:
            new_subjects.append((title, pairs, grade))
    return new_subjects

def main():
    subjects = build_subjects()
    print_table(subjects)
    print("Pairs per week:", total_pairs(subjects))

    mp = most_pairs(subjects)
    print(f"Most pairs: {mp[0]} ({mp[1]})")

    wk = weakest(subjects)
    print(f"Weakest subject: {wk[0]} ({wk[2]})")

    print("Titles:", titles_list(subjects))
    print(f"Grades: {grades_list(subjects)}, average: {average_grade(subjects):.2f}")

    print("Grade 10+:", grade_10_plus(subjects))

    print_histograms(subjects)

    subjects = retake_lowest(subjects)
    print("Subjects:", subjects)

if __name__ == "__main__":
    main()