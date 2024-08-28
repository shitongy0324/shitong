def name(new_name, list_name):
    if new_name in list_name:
        return False
    else:
        return True


list_name = []
while True:
    enter_name = input("please enter a name(enter space to exit program)")
    if enter_name != " ":
        if enter_name in list_name:
            print("Existing name")
        else:
            print("New name")
            list_name.append(enter_name)
    else:
        set_name = set(list_name)
        print(f"name:{set_name}")
        break
