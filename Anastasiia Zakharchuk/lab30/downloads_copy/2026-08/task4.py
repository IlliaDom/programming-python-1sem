score = int(input("Enter your score (0-100): "))
missed = int(input("Enter the number of missed classes: "))

if score < 0 or score > 100:
    print("Error: score must be between 0 and 100")
else:
    if score >= 90:
        letter = "A"
        ects = "відмінно"
    elif score >= 82:
        letter = "B"
        ects = "добре"
    elif score >= 74:
        letter = "C"
        ects = "добре"
    elif score >= 64:
        letter = "D"
        ects = "задовільно"
    elif score >= 60:
        letter = "E"
        ects = "задовільно"
    else:
        letter = "F"
        ects = "незадовільно"

    total_classes = 16
    not_admitted = missed / total_classes > 0.3

    if not_admitted:
        print("Warning: too many missed classes, not admitted to the exam")

    passed = letter != "F" and not not_admitted
    status = "passed" if passed else "failed"

    print(f"Score: {score}, Grade: {letter} ({ects}), Result: {status}")