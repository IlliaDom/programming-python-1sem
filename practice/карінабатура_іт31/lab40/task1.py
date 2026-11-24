class Student:
    def __init__(self, name: str, surname: str, group: str, birth_year: int) -> None:
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year

    def full_name(self) -> str:
        return f"{self.name} {self.surname}"

    def age(self, year: int) -> int:
        return year - self.birth_year

    def card(self, year: int = 2026) -> str:
        lines = [
            self.full_name(),
            f"group: {self.group}",
            f"age in {year}: {self.age(year)}",
        ]
        width = max(len(line) for line in lines)
        border = "+" + "-" * (width + 2) + "+"
        body = "\n".join(f"| {line:<{width}} |" for line in lines)
        return f"{border}\n{body}\n{border}"


if __name__ == "__main__":
    student_1 = Student("Каріна", "Батура", "ІТ-31", 2009)
    student_2 = Student("Олена", "Коваль", "ІТ-31", 2008)

    print(student_1.card(2026))
    print(student_2.card(2026))