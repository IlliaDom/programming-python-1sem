me = {
"name": "Sasha",
    "surname": "Romanitch",
    "group": "IT-32",
    "city": "Lutsk",
    "birth_year": 2009,
    "hobbies": ["swimming", "horse riding", "draw", "reading book"]
}
for key, value in me.items():
    print(f"{key}: {value}")

print("Ключі:", list(me.keys()))
print("Кількість пар:", len(me))

print("Група:", me["group"])
print("Email (get):", me.get("email", "unknown"))

me["email"] = "sascha.romanitcho@student.edu.ua"
me["city"] = "Lutsk"
removed_year = me.pop("birth_year")
print("Вилучене значення birth_year:", removed_year)
print("Словник після змін:", me)

print("Чи є ключ 'phone':", "phone" in me)
