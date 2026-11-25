from student import Student


def main() -> None:
    # TODO: заміни на свої справжні дані
    me = Student(name="Назар", surname="Прізвище", group="ГР-11", birth_year=2006)
    groupmate = Student(name="Іван", surname="Петренко", group="ГР-11", birth_year=2005)

    print(me.card())
    print()
    print(groupmate.card())


if __name__ == "__main__":
    main()
