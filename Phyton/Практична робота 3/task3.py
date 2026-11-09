a = float(input("Enter the first number: "))
op = input("Enter the operation (+, -, *, /, //, %, **): ")
b = float(input("Enter the second number: "))

if op == "+":
    print(f"{a} + {b} = {a + b:.4f}")
elif op == "-":
    print(f"{a} - {b} = {a - b:.4f}")
elif op == "*":
    print(f"{a} * {b} = {a * b:.4f}")
elif op == "/":
    if b == 0:
        print("Error: division by zero is not allowed")
    else:
        print(f"{a} / {b} = {a / b:.4f}")
elif op == "//":
    if b == 0:
        print("Error: integer division by zero is not allowed")
    else:
        print(f"{a} // {b} = {a // b:.4f}")
elif op == "%":
    if b == 0:
        print("Error: taking the remainder modulo zero is not allowed")
    else:
        print(f"{a} % {b} = {a % b:.4f}")
elif op == "**":
    print(f"{a} ** {b} = {a ** b:.4f}")
else:
    print(f"Unknown operation: {op}")