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
        return f"age in {year}: {year - self.birth_year}"

    def card(self):
        return f"""{self.full_name()}
group: {self.group}
{self.age(2026)}"""

oleksandr = Student("Oleksandr", "Romaniuk", "IT-31", 2008)
print("From class:", Student.college)
print("From object:", oleksandr.college)

tymophiy = Student("Tymophiy", "Savchuk", "IT-31", 2008)
tymophiy.college = "KTBP SNU"
print("From object oleksandr:", oleksandr.college)
print("From object tymophiy:", tymophiy.college)
print(oleksandr.__dict__)
print(tymophiy.__dict__)
print(Student.__dict__)

print("Count:", Student.__dict__["count"])