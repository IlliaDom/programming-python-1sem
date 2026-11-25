
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
            f"{self.full_name()} | "
            f"{self.group} | "
            f"age: {self.age(2026)}"
        )


student1 = Student("Ілля", "Воробей", "ІТ-31", 2009)
student2 = Student("Ім'я", "Прізвище", "ІТ-31", 2009)

print("College through class:", Student.college)
print("College through object:", student1.college)

student1.college = "Other college"

print("\nAfter changing college:")
print("Student 1:", student1.college)
print("Student 2:", student2.college)
print("Class:", Student.college)

print("\nStudents count:", Student.count)

print("\nStudent dictionary:")
print(student1.__dict__)

print("\nClass dictionary:")
print("college" in Student.__dict__)
print("college" in student1.__dict__)
