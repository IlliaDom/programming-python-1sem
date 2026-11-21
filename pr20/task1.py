NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"

LEADER_NAME = "Andriy"
LEADER_SURNAME = "Hordiy"
LEADER_PHONE = "+380 67 000 00 00"


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


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    me = Student(NAME, SURNAME, GROUP)
    leader = GroupLeader(LEADER_NAME, LEADER_SURNAME, GROUP, LEADER_PHONE)
    print(me.describe())
    print(leader.describe())


if __name__ == "__main__":
    main()
