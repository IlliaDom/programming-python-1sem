#Батури Каріни ІТ - 31
full_name = "   bATURA   kARINA   vITALIIVNA   "
#1 Завдання
print(full_name)
#2 Завдання
clean_name = " ".join(full_name.split()).title()
print("Змінене:",clean_name) 
print("Довжина рядка:", len(clean_name))
#3 Завдання
surname, name, patronymic = clean_name.split()
print("Перший і останній символ прізвища:", surname[0], surname[-1])
print("Прізвище навпаки:", surname[::-1])
print(f"Імʼя у форматі: {surname} {name[0]}. {patronymic[0]}.")
print(f"Ініціали без крапок: {surname[0]}{name[0]}{patronymic[0]}")
#4
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in clean_name if char in vowels)
print("Кількість голосних у повному імені:", vowel_count)
#5
group = "IT-31"
dash_index = group.find("-")
prefix = group[:dash_index]
suffix = group[dash_index + 1:]
print(f"Частина до дефіса: {prefix}, частина після: {suffix}")
print("Чи є частина після дефіса числом:", suffix.isdigit())
#6
login = f"{name[0].lower()}.{surname.lower()}"
email = f"{login}@student.edu.ua"
print("Логін:", login)
print("Пошта:", email)