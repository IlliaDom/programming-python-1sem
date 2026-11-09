print("Enter an integer: ")
num = int(input())

if num < 0:
    print("The number is negative")
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
    if 10 <= abs(num) <= 99:
        print("The number is two-digit")
elif num > 0:
    print("The number is positive")
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
    if 10 <= num <= 99:
        print("The number is two-digit")
else:
    print("The number is zero")
    