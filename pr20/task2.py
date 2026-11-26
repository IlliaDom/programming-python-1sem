from task1 import Person, Student, GroupLeader

me = Student("Nazarii", "Mischuk", "IT-32")
leader = GroupLeader("Bogdana", "Tscuhovych", "IT-32", "01234567")
person = Person("Nazarii", "Mischuk")

classes = [Person, Student, GroupLeader]

print("isinstance()")
for obj_name, obj in [("person", person), ("me", me), ("leader", leader)]:
    for cls in classes:
        print(f"{obj_name:<8} {cls.__name__:<12} {isinstance(obj, cls)}")

print()
print("issubclass()")
for child in classes:
    for parent in classes:
        print(f"{child.__name__:<12} {parent.__name__:<12} {issubclass(child, parent)}")

print()
print("GroupLeader.__mro__")
for cls in GroupLeader.__mro__:
    print(cls.__name__)
