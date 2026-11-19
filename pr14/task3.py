import qrcode

# --- ВАШІ ДАНІ: замініть на справжні (латиницею) ---
NAME = "Ivan"
SURNAME = "Petrenko"
GROUP = "PZ-11"
EMAIL = "ivan.petrenko@example.com"

print(f"{NAME} {SURNAME}, {GROUP}")

text = f"{NAME} {SURNAME}, {GROUP}, {EMAIL}"
image = qrcode.make(text)
image.save("contact.png")
print("saved: contact.png")
