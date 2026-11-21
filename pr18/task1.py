NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"
BIRTH_YEAR = 2008

OTHER = ("Sofia", "Stotska", "IT-31", 2009)

YEAR = 2026


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

    def card(self, year=YEAR):
        lines = [self.full_name(),
                 f"group: {self.group}",
                 f"age in {year}: {self.age(year)}"]
        width = max(len(line) for line in lines)
        border = "+" + "-" * (width + 2) + "+"
        body = [f"| {line:<{width}} |" for line in lines]
        return "\n".join([border, *body, border])


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    me = Student(NAME, SURNAME, GROUP, BIRTH_YEAR)
    other = Student(*OTHER)
    print(me.card())
    print(other.card())


if __name__ == "__main__":
    main()
