class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe(self):
        return f"{self.first_name} {self.last_name}"


class Student(Person):
    def __init__(self, first_name, last_name, group):
        super().__init__(first_name, last_name)
        self.group = group

    def describe(self):
        return f"{super().describe()}, група {self.group}"


class GroupLeader(Student):
    def __init__(self, first_name, last_name, group, phone):
        super().__init__(first_name, last_name, group)
        self.phone = phone

    def describe(self):
        return (
            f"{super().describe()}, староста групи, "
            f"телефон: {self.phone}"
        )


if __name__ == "__main__":
    student = Student("Марія", "Вовк", "І-23")
    print("Студентка:", student.describe())

    print("\nВведіть справжні дані старости групи І-23:")
    first_name = input("Ім'я: ").strip()
    last_name = input("Прізвище: ").strip()
    phone = input("Телефон: ").strip()

    leader = GroupLeader(first_name, last_name, "І-23", phone)
    print("Староста:", leader.describe())
