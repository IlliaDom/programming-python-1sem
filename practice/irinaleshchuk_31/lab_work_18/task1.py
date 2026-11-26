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
            "+---------------------+\n"
            f"| {self.full_name():<20}|\n"
            f"| group: {self.group:<13}|\n"
            f"| age in 2026: {self.age(2026):<9}|\n"
            "+---------------------+"
        )


student1 = Student("Ira", "Leshchuk", "IT-31", 2009)
student2 = Student("Olena", "Ivanenko", "IT-31", 2008)

print(student1.card())
print(student2.card())

print("\nКоледж через клас:", Student.college)
print("Коледж через об'єкт:", student1.college)

student1.college = "Lutsk College"

print("\nПісля зміни:")
print("student1:", student1.college)
print("student2:", student2.college)

print("\nКількість студентів:", Student.count)

print("\nАтрибути student1:")
print(student1.__dict__)

print("\nАтрибути класу:")
print(Student.__dict__)