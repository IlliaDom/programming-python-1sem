import qrcode

NAME_SURNAME = "Oleksandra Romanich"
GROUP = "IT-32"

def main():
    print(f"{NAME_SURNAME}, {GROUP}")
    
    text = "Oleksandra Romanich, IT-32, oleksandra.romanich@example.com"
    image = qrcode.make(text)
    image.save("contact.png")
    print("saved: contact.png")

if __name__ == "__main__":
    main()