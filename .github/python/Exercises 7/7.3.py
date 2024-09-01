airport = {'6523': "Total Rf Heliport",
           '323361': "Aero B Ranch Airport",
           '6524': "Lowell Field",
           '6525': 'Epps Airpark',
           '6526': 'Newport Hospital & Clinic Heliport',
           '322127': 'Fulton Airport',
           '6527': 'Cordes Airport',
           '6528': 'Goldstone (GTS) Airport',
           '324424': 'Williams Ag Airport',
           '322658': 'Kitchen Creek Helibase Heliport'}


def new_airport():
    global airport
    new_name_airport = input("Enter the name of airport")
    new_ICAO_airport = input("Enter the ICAD")
    if (new_ICAO_airport in airport) or (new_name_airport in airport):
        print(f"the ICAO code {new_ICAO_airport} is already in the computer")
    else:
        airport[new_ICAO_airport] = new_name_airport
        print(f" A new {new_ICAO_airport} and {new_name_airport} are added in computer")


def airport_information():
    ICAO_airport = input("enter the ICAO code")
    if ICAO_airport in airport:
        print(f"the airport's name of {ICAO_airport} is {airport[ICAO_airport]} ")
    else:
        print(f"There is no information about {ICAO_airport} ")


while True:
    print("Airport Data Program")
    print("1. Add a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    choice = input("enter your choice (1/2/3)")
    if choice == "1":
        new_airport()
    elif choice == "2":
        airport_information()
    elif choice == "3":
        break
    else:
        print("Choose the correct number ")
        continue
