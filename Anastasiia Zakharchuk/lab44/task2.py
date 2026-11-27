from task1 import Person, Student, GroupLeader

me = Student("Anastasia", "Zakharchuk", "IT-32")
leader = GroupLeader("Bohgdana", "Csuhovuch", "IT-32", "+380 67 000 00 00")
person = Person("Ivan", "Petrenko")

classes = [Person, Student, GroupLeader]
objects = [("person", person), ("me", me), ("leader", leader)]

print("isinstance(object, class)")
print(f"{'':<10}" + "".join(f"{c.__name__:<14}" for c in classes))
for label, obj in objects:
    print(f"{label:<10}" + "".join(f"{str(isinstance(obj, c)):<14}" for c in classes))

print()
print("issubclass(class, class)")
print(f"{'':<14}" + "".join(f"{c.__name__:<14}" for c in classes))
for a in classes:
    print(f"{a.__name__:<14}" + "".join(f"{str(issubclass(a, b)):<14}" for b in classes))

print()
print(GroupLeader.__mro__)
