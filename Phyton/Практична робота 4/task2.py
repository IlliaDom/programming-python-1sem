name = "Sasha Romanitch"
group = "IT-32"
print(f"{name}, {group}")
number = int(input("Enter an integer: "))
original_number = number
n = abs(number)

if n == 0:
    digits_count = 1
    digits_sum = 0
    max_digit = 0
    min_digit = 0
    reversed_number = 0
else:
    digits_count = 0
    digits_sum = 0
    max_digit = 0
    min_digit = 9
    reversed_number = 0

    while n > 0:
        digit = n % 10

        digits_count += 1
        digits_sum += digit

        if digit > max_digit:
            max_digit = digit

        if digit < min_digit:
            min_digit = digit

        reversed_number = reversed_number * 10 + digit

        n //= 10

    if original_number < 0:
        reversed_number = -reversed_number

print(f"Digits: {digits_count}")
print(f"Sum of digits: {digits_sum}")
print(f"Max digit: {max_digit}, min digit: {min_digit}")
print(f"Reversed: {reversed_number}")