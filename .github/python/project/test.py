from geopy import distance
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


# def get_airport(continent):
#     cursor = conn.cursor()
#     qry = ("""SELECT name FROM airport
#      as t1
#      WHERE continent = ? and type != 'heliport' and t1.id>=(RAND()*(SELECT MAX(id) FROM airport))LIMIT 10
#      """)
#     try:
#         cursor.execute(qry, (continent,))
#         results = cursor.fetchall()
#         if results:
#             results_tup = tuple(results)
#             return results_tup
#         else:
#             return False
#     except Exception as e:
#         print(e)
#         print("error")
# print(f"{get_airport('NA')}")