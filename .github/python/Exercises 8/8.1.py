import mariadb
import sys

try:
    conn = mariadb.connect(
        user="root",
        password="19990324s",
        host="127.0.0.1",
        port=3306,
        database="test"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

airport = {}
cursor = conn.cursor()
qry = "SELECT * FROM airports"
try:
    cursor.execute(qry)
    results = cursor.fetchall()
    for row in results:
        ident = row[1]
        name = row[3]
        municipality = row[10]
        airport[ident] = [name, municipality]
except Exception as e:
    print(e)
    print("error")


def information_airport(user_ICDO):
    detail_airport = []
    if user_ICDO in airport:
        detail_airport = airport[user_ICDO]
        print(f"the airport's name of {user_ICDO} is {detail_airport[0]},located in {detail_airport[1]} ")
    else:
        print("there are no information in computer")


while True:
    number = input("Please input the ICAO to search the information about airport\t(use space to exit the program)")
    if number == "":
        print("exit the program")
        break
    else:
        information_airport(number)

cursor.close()
