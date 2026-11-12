class Student:
    """A student with basic data."""

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
        lines = [
            self.full_name(),
            f"group: {self.group}",
            f"age in 2026: {self.age(2026)}",
        ]
        border = "+" + "-" * 25 + "+"
        body = [f"| {line:<23} |" for line in lines]
        return "\n".join([border, *body, border])


me = Student("Anastasia", "Zakharhcuk", "IT-32", 2008)
mate = Student("Ivan", "Petrenko", "IT-32", 2007)

print(me.card())
print(mate.card())