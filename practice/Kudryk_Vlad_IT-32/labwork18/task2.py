from task1 import Student

print("Vlad Kudryk, IT-32")

s1 = Student("Vlad", "Kudryk", "IT-32", 2009)
s2 = Student("Ivan", "Petrenko", "IT-32", 2007)

print("college via class:", Student.college)
print("college via object:", s1.college)

s1.college = "Other college"
print("s1.college:", s1.college)
print("s2.college:", s2.college)
print("Student.college:", Student.college)

print("count:", Student.count)

print("s1.__dict__:", s1.__dict__)
print("s2.__dict__:", s2.__dict__)
print("Student.__dict__ college:", Student.__dict__["college"])