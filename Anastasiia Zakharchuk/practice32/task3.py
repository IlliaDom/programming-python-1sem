import qrcode

NAME = "Anastasia Zakharchuk"
GROUP = "IT-32"
EMAIL = "nastyazahc@gmail.com"

print(f"{NAME}, {GROUP}")

text = f"{NAME}, {GROUP}, {EMAIL}"
image = qrcode.make(text)
image.save("contact.png")
print("saved: contact.png")