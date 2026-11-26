"""Завдання 1. Наслідування Person -> Student -> GroupLeader."""


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def describe(self):
        return f"{self.name} {self.surname}"


class Student(Person):
    def __init__(self, name, surname, group):
        super().__init__(name, surname)
        self.group = group

    def describe(self):
        return f"{super().describe()}, {self.group}"


class GroupLeader(Student):
    def __init__(self, name, surname, group, phone):
        super().__init__(name, surname, group)
        self.phone = phone

    def describe(self):
        return f"{super().describe()}, group leader, {self.phone}"


if __name__ == "__main__":
    student = Student("Ivan", "Petrenko", "PZ-11")
    leader = GroupLeader("Olena", "Koval", "PZ-11", "+380 67 000 00 00")
    print(student.describe())
    print(leader.describe())
