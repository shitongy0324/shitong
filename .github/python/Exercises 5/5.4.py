city_list =[]
for i in range (5):
    city = input(f"enter the name of city ")
    city_list.append(city)
print("\nThe cities you entered are:")
for i in city_list:
    print(f"{i}")