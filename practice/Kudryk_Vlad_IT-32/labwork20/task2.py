from hierarchy import Person, Student, GroupLeader

classes = [Person, Student, GroupLeader]
objects = {
    "person": Person("Karina", "Pikul"),
    "student": Student("Vlad", "Kudryk", "IT-32"),
    "leader": GroupLeader("Nazariiiiiiiiiiiiiiiiiy", "Beeeeeeeeeeeeeeeeeeeeeest", "IT-32", "+380 (50) 669 31 65"),
}

print("issubclass(рядок, стовпець):")
print(f"{'':12}" + "".join(f"{c.__name__:>12}" for c in classes))
for a in classes:
    print(f"{a.__name__:12}" + "".join(f"{str(issubclass(a, b)):>12}" for b in classes))

print("\nisinstance(обʼєкт, клас):")
print(f"{'':12}" + "".join(f"{c.__name__:>12}" for c in classes))
for n, o in objects.items():
    print(f"{n:12}" + "".join(f"{str(isinstance(o, c)):>12}" for c in classes))

print("\nGroupLeader.__mro__:")
for c in GroupLeader.__mro__:
    print("  ", c.__name__)
