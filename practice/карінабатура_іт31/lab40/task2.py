class Student:
    college = "FKTBP VNU"
    count = 0

    def __init__(self, name: str, surname: str, group: str, birth_year: int) -> None:
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year
        Student.count += 1


if __name__ == "__main__":
    print("Через клас Student.college:", Student.college)

    s1 = Student("Каріна", "Батура", "ІТ-31", 2008)
    s2 = Student("Олена", "Коваль", "ІТ-31", 2008)

    print("s1.college:", s1.college)
    print("s2.college:", s2.college)
    print("Кількість створених студентів (Student.count):", Student.count)

    s1.college = "Інший заклад"

    print("\nПісля присвоєння s1.college = 'Інший заклад':")
    print("s1.college:", s1.college)
    print("s2.college:", s2.college)
    print("Student.college:", Student.college)

    print("\nВміст __dict__:")
    print("s1.__dict__:", s1.__dict__)
    print("s2.__dict__:", s2.__dict__)
    print("Student.__dict__['college']:", Student.__dict__["college"])
    print("Student.__dict__['count']:", Student.__dict__["count"])