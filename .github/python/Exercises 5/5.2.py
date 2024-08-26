numbers = []
while True:
    user=input("enter a number (or press enter to quit) ")
    if user=="":
        break
    else:
        number=float(user)
        numbers.append(number)
numbers.sort(reverse=True)
print(f"the five greatest number are:{numbers[:5]}")