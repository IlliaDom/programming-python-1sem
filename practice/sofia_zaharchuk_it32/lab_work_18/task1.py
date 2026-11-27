"""Lab 18, tasks 1 and 2: class Student."""


class Student:
    """A college student."""

    college = "FKTBP VNU"  # class attribute, shared by all students
    count = 0              # number of created students

    def __init__(self, name: str, surname: str, group: str, birth_year: int):
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year
        Student.count += 1

    def full_name(self) -> str:
        """Return name and surname."""
        return f"{self.name} {self.surname}"

    def age(self, year: int) -> int:
        """Return the age in the given year."""
        return year - self.birth_year

    def card(self) -> str:
        """Return a multi-line student card."""
        lines = [
            self.full_name(),
            f"group: {self.group}",
            f"age in 2026: {self.age(2026)}",
        ]
        width = max(19, max(len(line) for line in lines))
        border = "+" + "-" * (width + 2) + "+"
        body = [f"| {line:<{width}} |" for line in lines]
        return "\n".join([border, *body, border])


# My data
ME = ("Sofiia", "Zakharchuk", "IT-32", 2008)
CLASSMATE = ("Anna", "Kovalenko", "IT-32", 2008)


def main() -> None:
    print("Sofiia Zakharchuk, IT-32")
    me = Student(*ME)
    classmate = Student(*CLASSMATE)
    print(me.card())
    print(classmate.card())


if __name__ == "__main__":
    main()
