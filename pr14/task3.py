import qrcode

NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"
EMAIL = "katakatasinska1@gmail.com"

print(f"{NAME} {SURNAME}, {GROUP}")

text = f"{NAME} {SURNAME}, {GROUP}, {EMAIL}"
image = qrcode.make(text)
image.save("contact.png")
print("saved: contact.png")
