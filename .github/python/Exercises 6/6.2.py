import random


def dice(sided):
   return random.randint(1, sided)

user_sided = int(input("enter the max sideds"))
while True:
    number=dice(user_sided)
    if number == user_sided :
        print(f"rolled :{number}")
        break
    else:
        print(f"rolled :{number}")