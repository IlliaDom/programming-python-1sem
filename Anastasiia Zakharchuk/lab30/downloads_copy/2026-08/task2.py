number = int(input("Enter an integer: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

if number != 0:
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

    digits = len(str(abs(number)))
    if digits == 1:
        print("The number is one-digit")
    elif digits == 2:
        print("The number is two-digit")
    elif digits == 3:
        print("The number is three-digit")
    else:
        print("The number is multi-digit")