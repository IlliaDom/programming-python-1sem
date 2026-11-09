about="I study Python at college and I like chess"
words=about.split()
print("Кількість слів:",len(words))
print("Найдовше слово:",max(words,key=len))
print("Слова у зворотному порядку:"," ".join(words[::-1]))
print("Літера 'a' трапляється:",about.lower().count("a"),"разів")
print("З великої літери:",about.title())
print("З підкресленнями:",about.replace(" ","_"))
def is_palindrome(text):
    cleaned=text.replace(" ","").lower()
    return cleaned==cleaned[::-1]
print("Перевірка 'Taras':",is_palindrome("Taras"))
print("Перевірка 'Never odd or even':",is_palindrome("Never odd or even"))
name="Taras"
day=3
encrypted=""
for ch in name:
    if ch.isalpha():
        base=ord('A') if ch.isupper() else ord('a')
        encrypted+=chr((ord(ch)-base+day)%26+base)
    else:
        encrypted+=ch
decrypted=""
for ch in encrypted:
    if ch.isalpha():
        base=ord('A') if ch.isupper() else ord('a')
        decrypted+=chr((ord(ch)-base-day)%26+base)
    else:
        decrypted+=ch
print("Зашифроване імʼя:",encrypted)
print("Розшифроване імʼя:",decrypted)