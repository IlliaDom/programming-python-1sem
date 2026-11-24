#Батури Каріни ІТ - 31
about = "I study software engineering and I love 3D modeling in Blender."
day = 23

# 1.
words = about.split()
print("Кількість слів:", len(words))

longest_word = max(words, key=len)
print(f"Найдовше слово: '{longest_word}'")

reversed_words = " ".join(reversed(words))
print("Слова у зворотному порядку:", reversed_words)

# 2
count_a = about.lower().count("a")
print("Кількість літер 'a':", count_a)

# 3
print("Кожне слово з великої:", about.title())
print("Заміна пробілів на підкреслення:", about.replace(" ", "_"))

# 4
def is_palindrome(text):
    clean_text = "".join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]

my_name = "Karina"
print(f"Чи є '{my_name}' паліндромом?:", is_palindrome(my_name))
print("Чи є 'Never odd or even' паліндромом?:", is_palindrome("Never odd or even"))

# 5
def caesar(text, shift):
    result = []
    for char in text:
        if "a" <= char <= "z":
            position = (ord(char) - ord("a") + shift) % 26
            result.append(chr(ord("a") + position))
        elif "A" <= char <= "Z":
            position = (ord(char) - ord("A") + shift) % 26
            result.append(chr(ord("A") + position))
        else:
            result.append(char)
    return "".join(result)

encrypted = caesar(my_name, day)
decrypted = caesar(encrypted, -day)

print(f"Зашифроване ім'я ({my_name}):", encrypted)
print("Розшифроване назад:", decrypted)