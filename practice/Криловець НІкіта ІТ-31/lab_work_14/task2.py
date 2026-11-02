import qrcode

print("Nikita Krilovets, IT-31")

text = "Nikita Krilovets, IT-31, nikita.krilovets@gimn14.lutsk.ua"

image = qrcode.make(text)
image.save("contact.png")

print("saved: contact.png")
