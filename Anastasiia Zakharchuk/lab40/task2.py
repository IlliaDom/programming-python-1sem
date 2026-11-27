class Student:
    """A student with basic data."""
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
        lines = [
            self.full_name(),
            f"group: {self.group}",
            f"age in 2026: {self.age(2026)}",
        ]
        border = "+" + "-" * 25 + "+"
        body = [f"| {line:<23} |" for line in lines]
        return "\n".join([border, *body, border])


me = Student("Anastasia", "Zakharchuk", "IT-32", 2008)
mate = Student("Ivan", "Petrenko", "IT-32", 2007)

print(me.college, mate.college, Student.college)

me.college = "Other college"
print(me.college, mate.college, Student.college)

print("students:", Student.count)

print(me.__dict__)
print(mate.__dict__)
print("college" in me.__dict__, "college" in Student.__dict__)
print("college" in mate.__dict__)

