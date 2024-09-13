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


def country_airport(area_code):
    cursor = conn.cursor()
    qry = ("""SELECT type, COUNT(*) as count 
    FROM airports 
    WHERE iso_country = ?
    GROUP BY type 
    ORDER BY type
     """)
    try:
        cursor.execute(qry, (area_code,))
        results = cursor.fetchall()
        if results:
            for area_type, count in results:
                print(f"{area_type}:{count}")
        else:
            print("no information")
    except Exception as e:
        print(e)
        print("error")


while True:
    input_area_code = input("enter the area code (for example FI)use space to exit program").upper()
    if input_area_code != "":
        country_airport(input_area_code)
    else:
        print("exit the program")
        conn.close()
        break









# airport = {}
# cursor = conn.cursor()
# qry = "SELECT * FROM airports"
# try:
#     cursor.execute(qry)
#     results = cursor.fetchall()
#     for row in results:
#         ident = row[1]
#         name = row[3]
#         municipality = row[10]
#         airport[ident] = [name, municipality]
# except Exception as e:
#     print(e)
#     print("error")