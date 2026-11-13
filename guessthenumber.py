
import random

nummer = random.randint(1, 10)

gok = int(input("Raad een getal van 1 tot 10: "))

if gok == nummer:
    print("Goed geraden!")
else:
    print("Fout! Het getal was", nummer)
