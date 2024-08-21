class_1 = input(' enter the cabin class of a cruise ship ')
if class_1 == "LUX":
    print('upper-deck cabin with a balcony.')
elif class_1 == "A":
    print('above the car deck, equipped with a window.')
elif class_1 == "B":
    print(' windowless cabin above the car deck.')
elif class_1 == "C":
    print('windowless cabin below the car deck.')
else:
    print('Invalid cabin class')
