surname = "Romanitch"
letters = list(surname.lower())
c = len(letters)

print("Літери:", letters)
print("Довжина c:", c)

print("Перша:", letters[0])
print("Середня:", letters[c // 2])
print("Остання (спосіб 1):", letters[-1])
print("Остання (спосіб 2):", letters[c - 1])

print("Перші три:", letters[:3])
print("Усі, крім перших трьох:", letters[3:])
print("Кожна друга:", letters[::2])
print("У зворотному порядку:", letters[::-1])
print("Останні дві:", letters[-2:])
print("5 елементів з позиції c:", letters[c:c + 5])

unique = []
for ch in letters:
    if ch not in unique:
        unique.append(ch)
print("Unique:", unique)

has_repeats = False
for ch in unique:
    cnt = letters.count(ch)
    if cnt > 1:
        print(f"Літера '{ch}' трапляється {cnt} разів")
        has_repeats = True
if not has_repeats:
    print("No repeated letters")

print("В алфавітному порядку:", sorted(letters))