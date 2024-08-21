import random
number = random.randint(1,10)
while True:
    user_number = int(input("guess the number(1 to 10)"))
    if user_number>number:
        print("too high")
        continue
    elif user_number<number:
        print("too low")
        continue
    else:
        print("correct!")
        break
