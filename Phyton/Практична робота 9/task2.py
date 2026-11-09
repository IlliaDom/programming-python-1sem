grades_str = "85, 90, 78, 92, 88"
grades = [int(g) for g in grades_str.split(", ")]
print("Список оцінок:", grades)
average = sum(grades) / len(grades)
print(f"Середня оцінка: {average:.2f}")
print(f"Найвища оцінка: {max(grades)}")
print(f"Найнижча оцінка: {min(grades)}")
print("Оцінки через |:", " | ".join(str(g) for g in grades))
subjects_str = "База даних, Кібербезпека, Програмування, Англійська мова, Розробка веб-ресурсів"
subjects = [s.strip() for s in subjects_str.split(",")]
print("Список предметів:", subjects)
print(f"{'№':<5}{'Предмет':<30}{'Оцінка':<7}")
print("-" * 42)
for i, (subj, grade) in enumerate(zip(subjects, grades), start=1):
    print(f"{i:<5}{subj:<30}{grade:<7}")
longest_subject = max(subjects, key=len)
print(f"Найдовша назва предмета: {longest_subject}")
print(f"Кількість символів: {len(longest_subject)}")
