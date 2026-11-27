a = float(input("Enter the first number: "))
op = input("Enter the operation (+, -, *, /, //, %, **): ")
b = float(input("Enter the second number: "))

if op == "+":
    result = a + b
    print(f"{a} + {b} = {result:.4f}")
elif op == "-":
    result = a - b
    print(f"{a} - {b} = {result:.4f}")
elif op == "*":
    result = a * b
    print(f"{a} * {b} = {result:.4f}")
elif op == "/":
    if b == 0:
        print("Error: division by zero")
    else:
        result = a / b
        print(f"{a} / {b} = {result:.4f}")
elif op == "//":
    if b == 0:
        print("Error: division by zero")
    else:
        result = a // b
        print(f"{a} // {b} = {result:.4f}")
elif op == "%":
    if b == 0:
        print("Error: division by zero")
    else:
        result = a % b
        print(f"{a} % {b} = {result:.4f}")
elif op == "**":
    result = a ** b
    print(f"{a} ** {b} = {result:.4f}")
else:
    print("Error: unknown operation")