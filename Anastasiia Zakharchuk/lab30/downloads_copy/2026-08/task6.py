# Sixth task. Anastasia Zakharchuk it-32

name = input("Enter your name: ")
age = int(input("Enter your age: "))

is_age_in_range = 18 <= age <= 60
is_age_even = age % 2 == 0
both_conditions = is_age_in_range and is_age_even
at_least_one_condition = is_age_in_range or is_age_even
years_left_to_60 = 60 - age

print(f"{name}, your age is {age}.")
print(f"Is age between 18 and 60 (inclusive)? {is_age_in_range}")
print(f"Is age an even number? {is_age_even}")
print(f"Both conditions true at the same time? {both_conditions}")
print(f"At least one condition true? {at_least_one_condition}")
print(f"Years left until 60: {years_left_to_60}")