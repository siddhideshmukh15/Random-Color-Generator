import random

print("==== Random Color Generator ====")

red=random.randint(0,255)
green =random.randint(0,255)
blue=random.randint(0,255)

print("RGB Color:",red,green,blue)
print("Hex Color: #{:02X}{:02X}{:02X}". format(red,green,blue))