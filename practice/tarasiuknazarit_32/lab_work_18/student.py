class Student:
    college = "FKTBP VNU"  # атрибут класу - спільний для всіх студентів
    count = 0  # лічильник створених обʼєктів (теж атрибут класу)

    def __init__(self, name: str, surname: str, group: str, birth_year: int):
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year
        Student.count += 1  # рахуємо саме через імʼя класу, не self

    def full_name(self) -> str:
        return f"{self.name} {self.surname}"

    def age(self, year: int) -> int:
        return year - self.birth_year

    def card(self) -> str:
        lines = [
            self.full_name(),
            f"group: {self.group}",
            f"age in {_this_year()}: {self.age(_this_year())}",
        ]
        width = max(len(line) for line in lines) + 2
        border = "+" + "-" * (width + 1) + "+"
        body = "\n".join(f"| {line:<{width - 1}} |" for line in lines)
        return f"{border}\n{body}\n{border}"


def _this_year() -> int:
    import datetime

    return datetime.date.today().year
