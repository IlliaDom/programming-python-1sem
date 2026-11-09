score = int(input("Enter your score (0-100): "))
missed = int(input("Enter the number of missed classes: "))

if score < 0 or score > 100:
    print("Error: score must be between 0 and 100")
else:
    if score >= 90:
        grade = "A"
    elif score >= 82:
        grade = "B"
    elif score >= 74:
        grade = "C"
    elif score >= 64:
        grade = "D"
    elif score >= 60:
        grade = "E"
    else:
        grade = "F"

    total_classes = 16
    if missed > total_classes * 0.3:
        print("Warning: too many missed classes, not admitted")
        result = "failed"
    elif grade == "F":
        result = "failed"
    else:
        result = "passed"

    print(f"Score: {score}, Grade: {grade}, {result}")