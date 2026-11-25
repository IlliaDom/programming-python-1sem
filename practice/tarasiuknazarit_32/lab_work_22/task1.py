"""
Завдання 1. Клас Money.
Перевіряємо точність копійок проти float, різні валюти,
віднімання, множення, repr.
"""
from money import Money


def main() -> None:
    print(Money(0.1) + Money(0.2))

    # Точність: Money рахує в копійках (int), float - ні
    print("Money(0.1) + Money(0.2) == Money(0.3):", Money(0.1) + Money(0.2) == Money(0.3))
    print("0.1 + 0.2 == 0.3 (звичайний float):", 0.1 + 0.2 == 0.3)

    # Додавання різних валют заборонено
    try:
        Money(100, "UAH") + Money(10, "USD")
    except ValueError as exc:
        print(f"error: {exc}")

    a = Money(150.75)
    b = Money(50.25)
    print("a - b =", a - b)
    print("a * 2 =", a * 2)
    print("repr(a) =", repr(a))
    print("a < b:", a < b, "| b < a:", b < a)


if __name__ == "__main__":
    main()
