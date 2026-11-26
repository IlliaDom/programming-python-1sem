class Student:
    college = "FKTBP VNU"
    count = 0

    def __init__(self, name, surname, group, birth_year):
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year
        Student.count += 1

    def full_name(self):
        return f"{self.name} {self.surname}"

    def age(self, year):
        return year - self.birth_year

    def card(self):
        return (
            f"Ім'я: {self.full_name()}\n"
            f"Група: {self.group}\n"
            f"Вік: {self.age(2026)}"
        )


student1 = Student("Ira", "Leshchuk", "IT-31", 2009)
student2 = Student("Olena", "Ivanenko", "IT-31", 2008)

print(student1.card())
print(student2.card())

print("\nКоледж:", Student.college)
print("Кількість студентів:", Student.count)

student1.college = "Lutsk College"

print("\nПісля зміни коледжу:")
print("Перший студент:", student1.college)
print("Другий студент:", student2.college)

print("\nАтрибути об'єкта:")
print(student1.__dict__)

print("\nАтрибути класу:")
print(Student.__dict__)