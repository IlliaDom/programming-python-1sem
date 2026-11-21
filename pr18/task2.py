from task1 import BIRTH_YEAR, GROUP, NAME, OTHER, SURNAME, Student


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    me = Student(NAME, SURNAME, GROUP, BIRTH_YEAR)
    other = Student(*OTHER)

    print("college via class: ", Student.college)
    print("college via object:", me.college)

    me.college = "Another college"    
    print("after me.college = ...")
    print("  me.college:     ", me.college)
    print("  other.college:  ", other.college)
    print("  Student.college:", Student.college)

    print("me.__dict__:   ", me.__dict__)
    print("other.__dict__:", other.__dict__)
    print("'college' in Student.__dict__:", "college" in Student.__dict__)
    print("'count' in Student.__dict__:  ", "count" in Student.__dict__)

    print("students created:", Student.count)


if __name__ == "__main__":
    main()
