from people import GroupLeader, Student


def main() -> None:
    # TODO: заміни на свої справжні дані
    me = Student(name="Назар", surname="Прізвище", group="ГР-11")
    leader = GroupLeader(
        name="Олена", surname="Коваль", group="ГР-11", phone="+380 67 000 00 00"
    )

    print(me.describe())
    print(leader.describe())


if __name__ == "__main__":
    main()
