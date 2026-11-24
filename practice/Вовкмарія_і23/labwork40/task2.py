class Student:
    college = "FKTBP VNU"
    count = 0

    def __init__(self, name, surname, group, birth_year):
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year
        Student.count += 1

    def full_name(self):
        return f"{self.name} {self.surname}"


student1 = Student("Maria", "Vovk", "І-23", 2008)
student2 = Student("Olena", "Koval", "І-23", 2007)

print("college through class:", Student.college)
print("college through object:", student1.college)

student1.college = "My college"
print("student1 college:", student1.college)
print("student2 college:", student2.college)

print("Student.__dict__ college:", Student.__dict__["college"])
print("student1.__dict__:", student1.__dict__)
print("student2.__dict__:", student2.__dict__)
print("Student.count:", Student.count)

print("Пояснення: college спочатку є атрибутом класу. "
      "Коли я присвоюю student1.college нове значення, "
      "створюється атрибут екземпляра тільки для student1. "
      "У student2 значення залишається класним. "
      "count збільшується в конструкторі для кожного нового об'єкта.")
