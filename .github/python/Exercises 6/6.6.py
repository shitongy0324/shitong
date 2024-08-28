import math


def value(diameter, price):
    area = (diameter / 100 / 2) *(diameter / 100 / 2) * math.pi
    unit_price = area / price
    return unit_price


diameter_1, price_1 = map(float,
                          input("Please enter the diameter and price of the first pizza(separated by spaces)").split())
diameter_2, price_2 = map(float,
                          input("Please enter the diameter and price of the second pizza(separated by spaces)").split())
if value(diameter_1, price_1) < value(diameter_2, price_2):
    print("The second pizza is better")
elif value(diameter_1, price_1) > value(diameter_2, price_2):
    print("The first pizza is batter")
else:
    print("They are same")
