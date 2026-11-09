name = input("Enter your name: ")
if not name:
    name = "Anonymous"
age = int(input("Enter your age: "))
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
print(f"Hello, {name}!")
print(category);