name = "Sasha"
surname = "Romanitch"
group = "IT-32"

c = len(surname)

grades = [10, 7, 9, 11, 8, 6, 12, 9]

print(f"{name} {surname}, {group}")
print("Початковий список:", grades)
print("Кількість оцінок:", len(grades))
print("Сума:", sum(grades))
print("Найкраща:", max(grades))
print("Найгірша:", min(grades))
print(f"Середнє: {sum(grades) / len(grades):.2f}")

print("Від найкращої до найгіршої:", sorted(grades, reverse=True))
print("Оригінал незмінний:", grades)

sorted_desc = sorted(grades, reverse=True)
print("Три найкращі:", sorted_desc[:3])
print("Три найгірші:", sorted_desc[-3:])

worst = min(grades)
print("Найгірша оцінка на позиції:", grades.index(worst) + 1)

avg = sum(grades) / len(grades)
above = [g for g in grades if g > avg]
print("Вищі за середнє:", above, "кількість:", len(above))

print("Чи є 12:", 12 in grades)
print("Чи є 1:", 1 in grades)

grades.append(c % 12 + 1)
print("Після append:", grades)

grades.insert(0, 12)
print("Після insert(0, 12):", grades)

grades.remove(min(grades))
print("Після remove(min):", grades)

last = grades.pop()
print("Вилучено останню:", last, "->", grades)

print("Скільки разів трапляється 12:", grades.count(12))

result = grades.sort()
print("Значення, яке повернула операція сортування:", result)
print("Відсортований grades:", grades)
