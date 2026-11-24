import qrcode
text = "Andriy Hordiy IT-31, andriy.hordi6@gmail.com"
image = qrcode.make(text)
image.save("contact.png")
print("saved: contact.png")
