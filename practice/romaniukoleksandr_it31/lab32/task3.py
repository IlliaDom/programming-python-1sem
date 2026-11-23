import qrcode 

text = "Romaniuk Oleksandr, IT-31, romaniuksashko@gmail.com"
image = qrcode.make(text)
image.save("contact.png")
print("qrcode generated in contact.png")