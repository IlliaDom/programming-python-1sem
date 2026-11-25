
class Student:
    def __init__(self, name, surname, group, birth_year):
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year

    def full_name(self):
        return f"{self.name} {self.surname}"

    def age(self, year):
        return year - self.birth_year

    def card(self):
        return (
            "+---------------------+\n"
            f"| {self.full_name():<19} |\n"
            f"| group: {self.group:<12} |\n"
            f"| age in 2026: {self.age(2026):<10} |\n"
            "+---------------------+"
        )


student1 = Student("Ілля", "Воробей", "ІТ-31", 2009)

# Замінити на справжні дані одногрупника
student2 = Student("Ім'я", "Прізвище", "ІТ-31", 2009)

print(student1.card())
print(student2.card())
