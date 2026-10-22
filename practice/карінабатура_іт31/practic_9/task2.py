#Батури Каріни ІТ - 31
grades_str = "95, 88, 100, 73, 81"

grades = [int(score) for score in grades_str.split(", ")]

avg_grade = sum(grades) / len(grades)
print(f"Середня оцінка: {avg_grade:.2f}")
print("Найвища оцінка:", max(grades))
print("Найнижча оцінка:", min(grades))

print("Оцінки:", " | ".join(str(g) for g in grades))

subjects_str = "Programming, Mathematics, Web Development, Databases, English"
subjects = [sub.strip() for sub in subjects_str.split(",")]

print("\n" + "=" * 35)
print(f"{'№':<3} | {'Предмет':<20} | {'Оцінка':>5}")
print("-" * 35)
for index, (subject, grade) in enumerate(zip(subjects, grades), start=1):
    print(f"{index:<3} | {subject:<20} | {grade:>5}")
print("=" * 35 + "\n")

longest_subject = max(subjects, key=len)
print(f"Найдовша назва предмета: '{longest_subject}' ({len(longest_subject)} символів)")