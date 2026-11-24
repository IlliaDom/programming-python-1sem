from task1 import Person, Student, GroupLeader


def print_issubclass_table(classes: list[type]) -> None:
    print("=== issubclass(Sub, Base) ===")
    header = f"{'Sub \\ Base':<15}" + "".join(f"{cls.__name__:>15}" for cls in classes)
    print(header)
    print("-" * len(header))
    for sub in classes:
        row = f"{sub.__name__:<15}"
        for base in classes:
            row += f"{str(issubclass(sub, base)):>15}"
        print(row)


def print_isinstance_table(objects: dict[str, object], classes: list[type]) -> None:
    print("\n=== isinstance(obj, Class) ===")
    header = f"{'Object':<15}" + "".join(f"{cls.__name__:>15}" for cls in classes)
    print(header)
    print("-" * len(header))
    for obj_name, obj in objects.items():
        row = f"{obj_name:<15}"
        for cls in classes:
            row += f"{str(isinstance(obj, cls)):>15}"
        print(row)


if __name__ == "__main__":
    classes = [Person, Student, GroupLeader]

    person_obj = Person("Іван", "Петренко")
    student_obj = Student("Каріна", "Батура", "ІТ-31")
    leader_obj = GroupLeader("Олена", "Коваль", "ІТ-31", "+380 67 000 00 00")

    objects = {
        "person_obj": person_obj,
        "student_obj": student_obj,
        "leader_obj": leader_obj,
    }

    print_issubclass_table(classes)
    print_isinstance_table(objects, classes)

    print("\n=== GroupLeader.__mro__ ===")
    for cls in GroupLeader.__mro__:
        print(" ->", cls)