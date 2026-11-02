import qrcode

text = "Yaroslav Korolchuk, IT-31, -007jarik@gmail.com"
image = qrcode.make(text)
image.save("contact.png")
print("saved: contact.png")
