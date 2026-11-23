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
        return self.name + " " + self.surname

    def age(self, year):
        return year - self.birth_year

    def card(self):
        lines = [
            self.full_name(),
            "group: " + self.group,
            "age in 2026: " + str(self.age(2026)),
        ]
        width = max(len(line) for line in lines)
        border = "+" + "-" * (width + 2) + "+"
        result = [border]
        for line in lines:
            result.append("| " + line.ljust(width) + " |")
        result.append(border)
        return "\n".join(result)


if __name__ == "__main__":
    print("Vlad Kudryk, IT-32")

    s1 = Student("Vlad", "Kudryk", "IT-32", 2009)
    s2 = Student("Ivan", "Petrenko", "IT-32", 2007)

    print(s1.card())
    print(s2.card())