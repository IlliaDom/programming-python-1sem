day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

if year <= 0:
    print(f"Date is invalid: year {year} must be positive")
elif month < 1 or month > 12:
    print(f"Date is invalid: month {month} is out of range 1-12")
else:
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days_in_month = 29
        else:
            days_in_month = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        days_in_month = 30
    else:
        days_in_month = 31

    if day < 1:
        print(f"Date is invalid: day {day} must be positive")
    elif day > days_in_month:
        print(f"Date is invalid: month {month} has only {days_in_month} days")
    else:
        print(f"Date is valid: {day:02d}.{month:02d}.{year}");