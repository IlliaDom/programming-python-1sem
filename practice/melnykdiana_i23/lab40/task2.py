class Student:
    college = "FKTBP VNU"  # атрибут класу, спільне початкове значення
    count = 0

    def __init__(self, name: str, surname: str, group: str, birth_year: int) -> None:
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year
        Student.count += 1

    def full_name(self) -> str:
        return f"{self.name} {self.surname}"


def main() -> None:
    diana = Student("Діана", "Мельник", "І-23", 2008)
    classmate = Student("Одногрупник", "(дані не надані)", "І-23", 2008)

    print("college через клас:", Student.college)
    print("college через об'єкт:", diana.college)
    print("до зміни, другий об'єкт:", classmate.college)

    diana.college = "ФКТБП ВНУ імені Лесі Українки"
    print("після зміни diana.college:", diana.college)
    print("значення college у другого об'єкта:", classmate.college)
    print("Student.count:", Student.count)

    print("\ndiana.__dict__:", diana.__dict__)
    print("classmate.__dict__:", classmate.__dict__)
    print("Student.__dict__['college']:", Student.__dict__["college"])
    print("Student.__dict__['count']:", Student.__dict__["count"])


if __name__ == "__main__":
    main()
