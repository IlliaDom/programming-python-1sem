schedule = {
    "Mon": ["Адміністрування операційни систем та комп'ютерних мереж", "Програмування", "Українська мова за професійним спрямуваннм"],
    "Tue": ["База даних в інформаційних системах", "Програмування", "IT-право"],
    "Wed": ["Розробка веб-ресурсів", "Іноземна мова за професійним спрямуванням", "База даних в інформаційних системах"],
    "Thu": ["Адміністрування операційних систем та комп'ютерних мереж", "Програмування", "Розробка веб-ресурсів"],
    "Fri": ["IT-право", "Іноземна мова за професійним спрямуванням", "База даних в інформаційних системах"],
}

print("=" * 60)
print(f"{'День':<6}{'Пар':<6}{'Предмети'}")
print("=" * 60)
for day, subjects in schedule.items():
    print(f"{day:<6}{len(subjects):<6}{', '.join(subjects)}")
print("=" * 60)

total = sum(len(subjects) for subjects in schedule.values())
print(f"Загальна кількість пар на тиждень: {total}")

busiest_day = max(schedule, key=lambda d: len(schedule[d]))
print(f"Найбільше пар у день: {busiest_day} ({len(schedule[busiest_day])})")

all_subjects = set()
for subjects in schedule.values():
    all_subjects.update(subjects)
print(f"\n Усі предмети ({len(all_subjects)}): {sorted(all_subjects)}")

mon = set(schedule["Mon"])
wed = set(schedule["Wed"])

common = mon & wed
only_mon = mon - wed

print(f"\nСпільні предмети Mon та Wed: {sorted(common) if common else '—'}")
print(f"Предмети тільки в Mon (немає в Wed): {sorted(only_mon) if only_mon else '—'}")


def subject_counts(schedule):
    counts = {}
    for subjects in schedule.values():
        for subject in subjects:
            counts[subject] = counts.get(subject, 0) + 1
    return counts


counts = subject_counts(schedule)

print("\nРейтинг предметів:")
rating = sorted(counts.items(), key=lambda item: item[1], reverse=True)
for i, (subject, count) in enumerate(rating, start=1):
    print(f"{i}. {subject} — {count}")