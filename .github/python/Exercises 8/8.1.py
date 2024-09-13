import mariadb
import sys

try:
    conn = mariadb.connect(
        user="root",
        password="19990324s",
        host="127.0.0.1",
        port=3306,
        database="flight_game"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


def information_airport(user_ICDO):
    airport = {}
    try:
        qry = ("SELECT name,municipality FROM airport "
               "WHERE ident = ?")
        cursor = conn.cursor()
        cursor.execute(qry, (user_ICDO,))
        results = cursor.fetchall()
        if results:
            for name, municipality in results:
                print(f"the airport's name of {user_ICDO} is {name},located in {municipality} ")
        else:
            print("there are no information in computer")
    except Exception as e:
        print(e)
        print("error")


while True:
    number = input(
        "Please input the ICAO to search the information about airport\n(use space to exit the program)").upper()
    if number == "":
        print("exit the program")
        break
    else:
        information_airport(number)
