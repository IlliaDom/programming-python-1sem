def get_initials(name: str, surname: str) -> str:
    return f"{name[0].upper()}.{surname[0].upper()}."

def count_letters(text: str, letter: str = "a") -> int:
    return text.lower().count(letter.lower())

def count_vowels(text: str) -> int:
    vowels = "aeiouy"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

def reverse_text(text: str) -> str:
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text
if __name__ == "__main__":
    name = "Sasha"
    surname = "Romanitch"
    group = "IT-32"
    print(f"{name} {surname}, {group}")
    initials = get_initials(name, surname)
    print(f"Initials: {initials}")
    surname_length = len(surname)
    vowels_count = count_vowels(surname)
    consonants_count = surname_length - vowels_count
    print(f"Letters in surname: {surname_length}")
    print(f"Vowels: {vowels_count}, consonants: {consonants_count}")
    for vowel in "aeiou":
        count = count_letters(surname, letter=vowel)
        print(f"{vowel}: {count}")
    default_count = count_letters(surname)
    print(f"Default letter 'a': {default_count}")
    reversed_surname = reverse_text(surname)
    print(f"Reversed surname: {reversed_surname}")
    print(f"Docstring: {count_letters.__doc__}")
    print(f"Annotations: {count_letters.__annotations__}")