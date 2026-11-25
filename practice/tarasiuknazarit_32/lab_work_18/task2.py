from student import Student


def main() -> None:
    # TODO: заміни на свої справжні дані
    s1 = Student(name="Назар", surname="Прізвище", group="ГР-11", birth_year=2006)
    s2 = Student(name="Іван", surname="Петренко", group="ГР-11", birth_year=2005)

    print("college через клас:", Student.college)
    print("college через обʼєкт s1:", s1.college)
    print("college через обʼєкт s2:", s2.college)

    # Створюємо студенту s1 ВЛАСНИЙ атрибут college. Він не чіпає
    # атрибут класу і не впливає на s2 - це новий ключ у s1.__dict__,
    # який просто "затуляє" (shadow) атрибут класу для цього обʼєкта.
    s1.college = "KNU"

    print("\nпісля s1.college = 'KNU':")
    print("college через клас:", Student.college)
    print("college через обʼєкт s1:", s1.college)  # власний атрибут
    print("college через обʼєкт s2:", s2.college)  # досі атрибут класу

    print("\ns1.__dict__:", s1.__dict__)
    print("s2.__dict__:", s2.__dict__)
    print("Student.__dict__ (фрагмент):", {
        k: v for k, v in Student.__dict__.items() if not k.startswith("__")
    })

    print("\nстворено студентів:", Student.count)


if __name__ == "__main__":
    main()
