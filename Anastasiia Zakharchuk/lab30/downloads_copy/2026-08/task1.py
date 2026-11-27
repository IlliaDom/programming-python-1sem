name = input("Введіть ім'я: ")

if not name:
    print("Ім'я не введено, буде використано Anonymous")
    name = "Anonymous"

age = int(input("Введіть вік: "))

if age < 0:
    category = "некоректне значення"
elif age <= 6:
    category = "child"
elif age <= 17:
    category = "schoolchild"
elif age <= 64:
    category = "adult"
else:
    category = "senior"

print(f"Привіт, {name}! Твоя категорія: {category}")