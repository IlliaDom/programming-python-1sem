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
            f"| {self.full_name():<19} |\n"
            f"| group: {self.group:<13} |\n"
            f"| age in 2026: {self.age(2026):<10} |\n"
            "+---------------------+"
        )


student1 = Student("Mushka", "Vlad", "IT31", 2009)

student2 = Student("Krylovets", "Nikita", "IT31", 2009)

print(student1.card())
print(student2.card())

print("College:", Student.college)
print("College:", student1.college)

student1.college = "My College"

print("Student 1 college:", student1.college)
print("Student 2 college:", student2.college)

print("Students count:", Student.count)

print("Student attributes:", student1.__dict__)
print("Class attributes:", Student.__dict__)
