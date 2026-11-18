import qrcode

text = "Diana Melnyk, I-23, d.melnyk@student.edu.ua"
image = qrcode.make(text)
image.save("contact.png")
print("saved: contact.png")
print(f"QR content: {text}")
