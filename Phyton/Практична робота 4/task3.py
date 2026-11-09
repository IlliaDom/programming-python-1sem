name = "Sasha"
surname = "Romanitch"

vowels = "aeiouy"

vowels_count = 0
consonants_count = 0

full_name = name + surname

print(name, surname)

for letter in full_name:
    if letter.lower() in vowels:
        vowels_count += 1
    else:
        consonants_count += 1

print(f"Vowels: {vowels_count}, consonants: {consonants_count}")
print(f"Total letters: {vowels_count + consonants_count}")