name = "Sasha Romanich"
group = "IT-32"

d = 30
c = 5

print(f"{name}, {group}")

count = 0
total = 0
product = 1
even = 0
odd = 0

print(f"Numbers from {d} to 31:", end=" ")

for number in range(d, 32):
    print(number, end=" ")

    count += 1
    total += number
    product *= number

    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print()

average = total / count

print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
print(f"Even: {even}, odd: {odd}")


count = 0
total = 0
product = 1
even = 0
odd = 0

number = d

print(f"Numbers from {d} to 31:", end=" ")

while number <= 31:
    print(number, end=" ")

    count += 1
    total += number
    product *= number

    if number % 2 == 0:
        even += 1
    else:
        odd += 1

    number += 1

print()

average = total / count

print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
print(f"Even: {even}, odd: {odd}")


print("Countdown:", end=" ")

for number in range(c, 0, -1):
    print(number, end=" ")

print()