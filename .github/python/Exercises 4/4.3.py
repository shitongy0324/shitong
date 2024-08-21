list = []
while True:
    a = str(input("Enter the number(use the space bar to exit the program)"))
    if a == " ":
        if len(list) == 0:
            print("no number")
        else:
            print(f"the smallest and largest number is {max(list)} and {min(list)}")
            print("program end")
            break
    else:
        b = int(a)
        list.append(b)
        continue
