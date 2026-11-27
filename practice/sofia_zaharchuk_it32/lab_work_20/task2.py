from task1 import Person, Student, GroupLeader, ME, LEADER

print("Sofiia Zakharchuk, IT-32")

person = Person(ME[0], ME[1])
student = Student(*ME)
leader = GroupLeader(*LEADER)
classes = [Person, Student, GroupLeader]

print("\nisinstance(object, Class)")
print(f"{'object':<14}" + "".join(f"{c.__name__:>13}" for c in classes))
for label, obj in [("person", person), ("student", student), ("leader", leader)]:
    print(f"{label:<14}" + "".join(f"{str(isinstance(obj, c)):>13}" for c in classes))

print("\nissubclass(Class, Class)")
print(f"{'class':<14}" + "".join(f"{c.__name__:>13}" for c in classes))
for a in classes:
    print(f"{a.__name__:<14}" + "".join(f"{str(issubclass(a, b)):>13}" for b in classes))

print("\nGroupLeader.__mro__:")
print([cls.__name__ for cls in GroupLeader.__mro__])
print(leader.describe())
