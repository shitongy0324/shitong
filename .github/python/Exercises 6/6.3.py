def liter(gallon):
    float(gallon)
    return gallon * 3.785


while True:
    user_gallon = float(input("input gallons"))
    if user_gallon < 0:
        print("stop")
        break
    else:
        user_liter = liter(user_gallon)
        print(f"{user_gallon:.2f}gallons={user_liter:.2f}liters")
        continue
