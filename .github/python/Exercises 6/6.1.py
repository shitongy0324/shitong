import random


def dice():
   return random.randint(1, 6)
while True:
    number=dice()
    if number == 6:
        print(f"rolled :{number}")
        break
    else:
        print(f"rolled :{number}")