class Student:
    def __init__(self, name: str, surname: str, group: str, birth_year: int) -> None:
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year

    def full_name(self) -> str:
        return f"{self.name} {self.surname}"

    def age(self, year: int) -> int:
        # Вік за роками; точна дата народження в умові не вказана.
        return year - self.birth_year

    def card(self, year: int = 2026) -> str:
        title = self.full_name()
        width = max(29, len(title) + 4, len(self.group) + 13, len(f"age in {year}: {self.age(year)}") + 4)
        border = "+" + "-" * (width - 2) + "+"
        rows = [title, f"group: {self.group}", f"age in {year}: {self.age(year)}"]
        return "\n".join([border, *(f"| {row:<{width - 4}} |" for row in rows), border])


def main() -> None:
    diana = Student("Діана", "Мельник", "І-23", 2008)
    classmate = Student("Одногрупник", "(дані не надані)", "І-23", 2008)
    print("Студентка:")
    print(diana.card())
    print("\nДругий об'єкт (демонстраційний, дані одногрупника потрібно замінити):")
    print(classmate.card())


if __name__ == "__main__":
    main()
