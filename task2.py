class Person:
    pass


class Student(Person):
    pass


class GroupLeader(Student):
    pass


person = Person()
student = Student()
leader = GroupLeader()

print("Перевірка isinstance:")
print("person — Person:", isinstance(person, Person))
print("student — Student:", isinstance(student, Student))
print("student — Person:", isinstance(student, Person))
print("leader — GroupLeader:", isinstance(leader, GroupLeader))
print("leader — Student:", isinstance(leader, Student))
print("leader — Person:", isinstance(leader, Person))
print("person — Student:", isinstance(person, Student))

print("\nПеревірка issubclass:")
print("Student → Person:", issubclass(Student, Person))
print("GroupLeader → Student:", issubclass(GroupLeader, Student))
print("GroupLeader → Person:", issubclass(GroupLeader, Person))
print("Person → Student:", issubclass(Person, Student))

print("\nПорядок MRO:")
print([cls.__name__ for cls in GroupLeader.__mro__])