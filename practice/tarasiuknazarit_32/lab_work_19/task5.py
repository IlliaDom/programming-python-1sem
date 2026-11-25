"""
Завдання 5. Деструктор.
Досліджуємо, коли саме викликається __del__: одразу після del,
коли є друге посилання на обʼєкт, і наприкінці програми.
"""
from wallet import Wallet

# Зберігаємо тут обʼєкт зі сценарію 3, щоб він дожив до кінця програми
leftover_wallet = None


def scenario_1_simple_del() -> None:
    print("--- сценарій 1: del wallet ---")
    w = Wallet("Сценарій1", 100)
    del w
    print("після del w (деструктор уже мав викликатись вище)")


def scenario_2_second_reference() -> None:
    print("--- сценарій 2: є друге посилання ---")
    w = Wallet("Сценарій2", 100)
    other = w  # other і w тепер вказують на той самий обʼєкт
    del w
    print("після del w: обʼєкт ще живий, бо на нього вказує 'other'")
    del other
    print("після del other: щойно зник останній зв'язок -> деструктор мав викликатись")


def scenario_3_end_of_program() -> None:
    global leftover_wallet
    print("--- сценарій 3: обʼєкт доживає до кінця програми ---")
    leftover_wallet = Wallet("Сценарій3", 100)
    print("обʼєкт створено і збережено в глобальній змінній")


def main() -> None:
    scenario_1_simple_del()
    print()
    scenario_2_second_reference()
    print()
    scenario_3_end_of_program()
    print()
    print("main() завершено; якщо деструктор 'Сценарій3' ще не "
          "спрацював - він викличеться під час завершення програми")


if __name__ == "__main__":
    main()
