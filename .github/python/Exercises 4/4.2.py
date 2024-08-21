while True:
    inches = float(input("enter a inches"))
    if inches < 0:
        print("Negative value entered. Program terminating")
        break
    else:
        cm = inches * 2.54
        print(f"{inches:.2f} inches = {cm:.2f} cm")
        continue