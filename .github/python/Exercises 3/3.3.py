gender = input("enter your biological gender (M/F) ")
if gender == "F":
    hemoglobin_value_1 = float(input("enter your hemoglobin value (g/l)"))
    if 117 <= hemoglobin_value_1 <= 155:
        print("normal")
    else:
        print("abnormal")
elif gender == "M":
    hemoglobin_value_2 = float(input("enter your hemoglobin value (g/l)"))
    if 134 <= hemoglobin_value_2 <= 167:
        print("normal")
    else:
        print("abnormal")
else:
    print("Please enter the correct information")
