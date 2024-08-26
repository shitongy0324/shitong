import random
sum_number = 0
dice = int(input("how many dices do you want to roll"))
for i in range(dice):
    numbers=random.randint(1,6)
    sum_number += numbers
print(f"sum of the number is {sum_number}")