full_name = "  rOMANITCH oleksandra oleksandrivna"
clean_name = " ".join(full_name.split()).title()
print("Охайний вигляд:", clean_name)
print("Довжина рядка:", len(clean_name))
print()
surname, name, patronymic = clean_name.split()
print("Перший символ прізвища:", surname[0])
print("Останній символ прізвища:", surname[-1])
print()
print("Прізвище навпаки:", surname[::-1])
print()
print(f"Формат Прізвище І. Б.: {surname} {name[0]}. {patronymic[0]}.")
print()
initials = surname[0] + name[0] + patronymic[0]
print("Ініціали без крапок:", initials)
print()
vowels = "aeiouAEIOUаеуоияієїюАЕУОИЯІЇЄЮ"
vowel_count = sum(1 for char in clean_name if char in vowels)
print("Кількість голосних:", vowel_count)
print()
group = "IT-32"
dash_index = group.find("-")
part_before = group[:dash_index]
part_after = group[dash_index + 1:]
print("Група:", group)
print("Частина до дефіса:", part_before)
print("Частина після дефіса:", part_after)
print("Частина після дефіса є числом:", part_after.isdigit())
print()
login = f"{name[0].lower()}.{surname.lower()}"
email = f"{login}@student.edu.ua"
print("Логін:", login)
print("Пошта:", email)