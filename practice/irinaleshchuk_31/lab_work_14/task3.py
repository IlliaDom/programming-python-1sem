import qrcode

contact = "Ira Leshchuk, IT-31, ira.leshchuk@example.com"

qr = qrcode.make(contact)
qr.save("contact.png")

print("QR-код успішно створено!")