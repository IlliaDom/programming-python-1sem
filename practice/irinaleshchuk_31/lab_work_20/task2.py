
from task1 import Person, Student, GroupLeader

student = Student("Ira", "Leshchuk", "IT-31")
leader = GroupLeader("Olena", "Koval", "IT-31", "+380 67 000 00 00")

print("Перевірка isinstance():")
objects = [student, leader]
classes = [Person, Student, GroupLeader]

for obj in objects:
    for cls in classes:
        print(f"{obj.__class__.__name__} належить до {cls.__name__}: {isinstance(obj, cls)}")

print("\nПеревірка issubclass():")
for cls in classes:
    for parent in classes:
        print(f"{cls.__name__} є нащадком {parent.__name__}: {issubclass(cls, parent)}")

print("\nПорядок MRO:")
print(GroupLeader.__mro__)
