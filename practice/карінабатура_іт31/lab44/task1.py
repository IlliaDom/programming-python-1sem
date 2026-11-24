class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def describe(self) -> str:
        return f"{self.name} {self.surname}"


class Student(Person):
    def __init__(self, name: str, surname: str, group: str):
        super().__init__(name, surname)
        self.group = group

    def describe(self) -> str:
        return f"{super().describe()}, {self.group}"


class GroupLeader(Student):
    def __init__(self, name: str, surname: str, group: str, phone: str):
        super().__init__(name, surname, group)
        self.phone = phone

    def describe(self) -> str:
        return f"{super().describe()}, group leader, {self.phone}"


if __name__ == "__main__":
    me = Student("Каріна", "Батура", "ІТ-31")
    leader = GroupLeader("Олена", "Коваль", "ІТ-31", "+380 67 000 00 00")

    print(me.describe())
    print(leader.describe())