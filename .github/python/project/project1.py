import mariadb
import sys
import pandas as pd

try:
    conn = mariadb.connect(
        user="root",
        password="19990324s",
        host="127.0.0.1",
        port=3306,
        database="project"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


# setup player
def player_setup():
    cursor = conn.cursor()
    qry = """SELECT ident,name from airport"""
    cursor.execute(qry)
    airports = cursor.fetchall()
    print("Select your initial airport(ident/name):")
    for airport in airports:
        print(f"{airport[0], {airport[1]} }")

    start_airport = int(input("enter the ident"))
    player_name = input("enter the player's name")

    cursor.execute(
        "INSERT INTO player_info (name,current_funds,current_airport,current_day) VALUES (%s,10000,%s,0)",
        (player_name, start_airport))
    conn.commit()


# View Target Airport Goods
def view_airport_goods(airport_ident):
    cursor=conn.cursor()
    cursor.execute("""SELECT name,buy_price,sell_price,stock FROM goods_in_different_airport,
    INNER JOIN goods ON """)

