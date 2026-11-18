class Student:
    def __init__(self, name, surname, group, birth_year):
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year

    def full_name(self):
        return f"{self.name} {self.surname}"

    def age(self, year):
        return f"age in {year}: {year - self.birth_year}"

    def card(self):
        return f"""{self.full_name()}
group: {self.group}
{self.age(2026)}"""

oleksandr = Student("Oleksandr", "Romaniuk", "IT-31", 2008)
print(oleksandr.card())

tymophiy = Student("Tymophiy", "Savchuk", "IT-31", 2008)
print(tymophiy.card())