def print_age(year):
    age = 2026 - year
    print(f"Age: {age}")
def get_age(year, current_year=2026):
    if year > current_year or year < 0:
        return -1
    
    age = current_year - year
    return age
y = 2007
print_age(y)
print(f"print_age returned: {print_age(y)}")
age = get_age(y)
print(f"Age from get_age: {age}")
print(f"Age in months: {age * 12}")
print(f"Age in weeks: {age * 52}")
age_in_2030 = get_age(y, current_year=2030)
print(f"Age in 2030: {age_in_2030}")
invalid_result = get_age(3000)
print(f"Invalid year 3000 gives: {invalid_result}")