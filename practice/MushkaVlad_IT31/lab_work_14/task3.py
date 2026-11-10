import qrcode

print("Mushka Vlad IT31")

text = "Vlad Mushka, IT31, vladmushka7@gmail.com"
image = qrcode.make(text)
image.save("contact.png")

print("saved: contact.png")
