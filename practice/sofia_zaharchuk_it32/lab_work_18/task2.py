"""Lab 18, task 2: class attribute and instance attribute."""

from task1 import CLASSMATE, ME, Student


def main() -> None:
    print("Sofiia Zakharchuk, IT-32")
    me = Student(*ME)
    classmate = Student(*CLASSMATE)

    print("\n1) college through the class and the objects")
    print("Student.college:  ", Student.college)
    print("me.college:       ", me.college)
    print("classmate.college:", classmate.college)

    print("\n2) change college for one object")
    me.college = "Other college"  # creates an instance attribute in me
    print("me.college:       ", me.college)
    print("classmate.college:", classmate.college)
    print("Student.college:  ", Student.college)

    print("\n3) created students:", Student.count)

    print("\n4) where the attributes are stored")
    print("me.__dict__:       ", me.__dict__)
    print("classmate.__dict__:", classmate.__dict__)
    print("college in Student.__dict__:", Student.__dict__["college"])
    print("count in Student.__dict__:  ", Student.__dict__["count"])


if __name__ == "__main__":
    main()
