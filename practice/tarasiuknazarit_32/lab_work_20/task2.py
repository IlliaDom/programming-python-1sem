from people import GroupLeader, Person, Student

CLASSES = [Person, Student, GroupLeader]
OBJECTS = {
    Person: Person("Назар", "Прізвище"),
    Student: Student("Назар", "Прізвище", "ГР-11"),
    GroupLeader: GroupLeader("Олена", "Коваль", "ГР-11", "+380 67 000 00 00"),
}


def print_isinstance_table() -> None:
    print("isinstance(obj_of_row, row_class_of_col):")
    header = "obj \\ class".ljust(14) + "".join(c.__name__.ljust(14) for c in CLASSES)
    print(header)
    for obj_cls in CLASSES:
        obj = OBJECTS[obj_cls]
        row = obj_cls.__name__.ljust(14)
        for check_cls in CLASSES:
            row += str(isinstance(obj, check_cls)).ljust(14)
        print(row)


def print_issubclass_table() -> None:
    print("\nissubclass(row, col):")
    header = "class".ljust(14) + "".join(c.__name__.ljust(14) for c in CLASSES)
    print(header)
    for row_cls in CLASSES:
        row = row_cls.__name__.ljust(14)
        for col_cls in CLASSES:
            row += str(issubclass(row_cls, col_cls)).ljust(14)
        print(row)


def print_mro() -> None:
    print("\nGroupLeader.__mro__:")
    for cls in GroupLeader.__mro__:
        print(" ", cls.__name__)
    print(
        "\nПояснення: GroupLeader.describe() знайдено одразу (власний метод).\n"
        "Якби GroupLeader свого describe() не мав, Python шукав би метод у\n"
        "порядку __mro__ зліва направо: спочатку в GroupLeader, потім у\n"
        "Student, потім у Person, і лише потім у object - перше знайдене\n"
        "визначення і буде використано."
    )


def main() -> None:
    print_isinstance_table()
    print_issubclass_table()
    print_mro()
    print(
        "\nisinstance(leader, Person) -> True, бо GroupLeader успадковує\n"
        "Student, а Student успадковує Person: обʼєкт GroupLeader за\n"
        "визначенням є одночасно і Student, і Person - уся ієрархія\n"
        "'вбудована' в нього."
    )


if __name__ == "__main__":
    main()
