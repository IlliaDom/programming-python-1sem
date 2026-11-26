"""Завдання 2. Перевірка належності об'єктів і порядок пошуку методів."""

from task1 import GroupLeader, Person, Student


def main():
    person = Person("Ivan", "Petrenko")
    student = Student("Ivan", "Petrenko", "PZ-11")
    leader = GroupLeader("Olena", "Koval", "PZ-11", "+380 67 000 00 00")
    classes = (Person, Student, GroupLeader)
    instances = (("person", person), ("student", student), ("leader", leader))

    print("issubclass:")
    print(f"{'клас':<14}" + "".join(f"{cls.__name__:<15}" for cls in classes))
    for child in classes:
        values = "".join(f"{str(issubclass(child, parent)):<15}" for parent in classes)
        print(f"{child.__name__:<14}{values}")

    print("\nisinstance:")
    object_header = "об'єкт"
    print(f"{object_header:<14}" + "".join(f"{cls.__name__:<15}" for cls in classes))
    for label, obj in instances:
        values = "".join(f"{str(isinstance(obj, cls)):<15}" for cls in classes)
        print(f"{label:<14}{values}")

    print("\nGroupLeader.__mro__:")
    print(" -> ".join(cls.__name__ for cls in GroupLeader.__mro__))
    print("describe(): GroupLeader -> Student -> Person -> object")


if __name__ == "__main__":
    main()
