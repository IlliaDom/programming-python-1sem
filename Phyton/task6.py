name = input("Enter your name: ")
age = int(input("Enter your age: "))

is_in_range = 18 <= age <= 45
is_even = age % 2 == 0
both_conditions = is_in_range and is_even
either_condition = is_in_range or is_even
years_to_45 = 45 - age

print()
print(f"Hello, {name}!")
print(f"Is your age between 18 and 45? Result: {is_in_range}")
print(f"Is your age an even number? Result: {is_even}")
print(f"Are both conditions True? Result: {both_conditions}")
print(f"Is at least one condition True? Result: {either_condition}")
print(f"Years left until 45: {years_to_45}")
