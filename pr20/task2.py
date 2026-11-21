from task1 import (GROUP, LEADER_NAME, LEADER_PHONE, LEADER_SURNAME, NAME,
                   SURNAME, GroupLeader, Person, Student)


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    me = Student(NAME, SURNAME, GROUP)
    leader = GroupLeader(LEADER_NAME, LEADER_SURNAME, GROUP, LEADER_PHONE)
    classes = [Person, Student, GroupLeader]

    print("\nisinstance(object, class):")
    print(f"{'object':<14}" + "".join(f"{c.__name__:<14}" for c in classes))
    for label, obj in [("me (Student)", me), ("leader", leader)]:
        print(f"{label:<14}" + "".join(
            f"{str(isinstance(obj, c)):<14}" for c in classes))

    print("\nissubclass(row, column):")
    print(f"{'':<14}" + "".join(f"{c.__name__:<14}" for c in classes))
    for a in classes:
        print(f"{a.__name__:<14}" + "".join(
            f"{str(issubclass(a, b)):<14}" for b in classes))

    print("\nGroupLeader.__mro__:")
    for cls in GroupLeader.__mro__:
        print("  ", cls.__name__)


if __name__ == "__main__":
    main()
