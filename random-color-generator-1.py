import random

print("===== Random Color Generator ====")

while True:
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)

    hex_color="#{:02X}{:02X}{:02X}".format(red,green,blue)
    print("\n RGB Color:",red,green,blue)
    print("HEX Color:",hex_color)

    again=input("\n Generate another color?(y/n):").lower()

    if again !="y":
        print("Thank you!")
        break