username = "python"
password = "rules"
i = 5
while 1<= i <= 5:
    i -= 1
    username_input = input("please enter the username")
    password_input = input("please enter the password")
    if username_input == username and password_input == password:
        print("welcome")
        break
    else:
        print(f"wrong You have {i:.0f} more chances.")
if i == 0:
    print("Access denied")
