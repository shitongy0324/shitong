from geopy import distance
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


def get_distance(ICAO_code):
    cursor = conn.cursor()
    qry = ("""SELECT latitude_deg , longitude_deg
    FROM airports 
    WHERE ident = ?
     """)
    try:
        cursor.execute(qry, (ICAO_code,))
        results = cursor.fetchall()
        if results:
            results_tup = tuple(results)
            return results_tup
        else:
            return False
    except Exception as e:
        print(e)
        print("error")


def Calculate_distance(ICAO1, ICAO2):
    area1=get_distance(ICAO1)
    area2=get_distance(ICAO2)
    if area2 and area1:
        distances=distance.distance(area2, area1).km
        print(f"the distance between {ICAO1} and {ICAO2} is {distances:.2f}km")
    else:
        print("no information")


while True:
    ICAO_1 =input("enter the first ICAO code(use space to exit)").strip().upper()
    ICAO_2 =input("enter the second ICAO code(use space to exit)").strip().upper()
    if (ICAO_1 or ICAO_2) == "":
        print("Exit")
        break
    else:
        Calculate_distance(ICAO_1, ICAO_2)





