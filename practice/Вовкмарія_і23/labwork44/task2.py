from task1 import Person, Student, GroupLeader


def main():
    classes = [Person, Student, GroupLeader]

    print("ТАБЛИЦЯ issubclass()")
    print(f"{'Клас':<15}", end="")
    for cls in classes:
        print(f"{cls.__name__:<15}", end="")
    print()

    for child in classes:
        print(f"{child.__name__:<15}", end="")
        for parent in classes:
            print(f"{str(issubclass(child, parent)):<15}", end="")
        print()

    student = Student("Марія", "Вовк", "І-23")
    leader = GroupLeader("Староста", "Групи", "І-23", "не вказано")

    print("\nПеревірки isinstance():")
    print("student — Student:", isinstance(student, Student))
    print("student — Person:", isinstance(student, Person))
    print("leader — GroupLeader:", isinstance(leader, GroupLeader))
    print("leader — Student:", isinstance(leader, Student))
    print("leader — Person:", isinstance(leader, Person))

    print("\nMRO класу GroupLeader:")
    for cls in GroupLeader.__mro__:
        print(cls.__name__)

    print("\nПорядок пошуку describe(): GroupLeader -> Student -> Person -> object.")
    print("isinstance(leader, Person) дорівнює True, оскільки GroupLeader")
    print("успадковує Student, а Student успадковує Person.")


if __name__ == "__main__":
    main()
