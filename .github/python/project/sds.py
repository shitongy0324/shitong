import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='project',
    user='root',
    password='19990324s',
    autocommit=True
)


def buy_goods(player_id):
    try:
        cursor = connection.cursor()
        # show airport goods
        cursor.execute('''SELECT goods_id, goods.name, buy_price, stock
                          FROM goods
                          JOIN project.goods_in_different_airport gida ON goods.id = gida.goods_id
                          JOIN game ON current_airport = airport_ident
                          WHERE game.player_id = %s''',
                       (player_id,))
        view_airport_goods = cursor.fetchall()
        view = pd.DataFrame(view_airport_goods, columns=["goods id", "goods name", "buy price", "stock"]).set_index(
            "goods id")
        print(view)

        # found player
        cursor.execute('''SELECT current_airport, current_funds FROM game WHERE player_id = %s''', (player_id,))
        current_airport, current_funds = cursor.fetchone()

        # get user input
        product_id = int(input("Enter the id number to be purchased: "))
        quantity = int(input("Enter quantity purchased: "))

        # search airport goods
        cursor.execute('''SELECT buy_price, stock FROM goods_in_different_airport 
                          WHERE airport_ident = %s AND goods_id = %s''', (current_airport, product_id,))
        product = cursor.fetchone()

        if product and quantity <= product[1]:
            total_cost = product[0] * quantity
            if total_cost <= current_funds:
                # update player funds
                cursor.execute("UPDATE game SET current_funds = current_funds - %s WHERE player_id = %s",
                               (total_cost, player_id,))
                # update player inventory
                cursor.execute('''INSERT INTO player_inventory (player_id, goods_id, quantity)
                                  VALUES(%s, %s, %s) 
                                  ON DUPLICATE KEY UPDATE quantity = quantity + %s''',
                               (player_id, product_id, quantity, quantity))
                # update airport stock
                cursor.execute('''UPDATE goods_in_different_airport SET stock = stock - %s
                                  WHERE airport_ident = %s AND goods_id = %s''',
                               (quantity, current_airport, product_id,))
                connection.commit()
                print(f'Successful purchase of {quantity} units (total cost: {total_cost})')
            else:
                print("Insufficient funds to purchase.")
        else:
            print("Insufficient stock or goods does not exist.")
    except Exception as e:
        return False


def sell_goods(player_id):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT current_airport FROM game WHERE player_id = %s', (player_id,))
        current_airport = cursor.fetchone()[0]

        # search player inventory
        cursor.execute('''SELECT player_inventory.goods_id, name, quantity, sell_price
                          FROM player_inventory
                          JOIN goods ON player_inventory.goods_id = goods.id
                          JOIN goods_in_different_airport ON goods_in_different_airport.goods_id = player_inventory.goods_id
                          WHERE airport_ident = %s AND player_id = %s''', (current_airport, player_id,))
        inventory = cursor.fetchall()

        if not inventory:
            print("You do not have any inventory to sell.")
            return

        print("\nYour inventory")
        inventory_view = pd.DataFrame(inventory,
                                      columns=["goods id", "goods name", "quantity", "sell price"]).set_index(
            "goods id")
        print(inventory_view)

        goods_id = int(input("Enter the goods number to be sold: "))
        quantity = int(input("Enter the quantity sold: "))

        # Checking the adequacy of stock
        cursor.execute('''SELECT quantity FROM player_inventory WHERE player_id = %s AND goods_id = %s''',
                       (player_id, goods_id,))
        stock = cursor.fetchone()

        if stock and quantity <= stock[0]:
            # get sell price
            cursor.execute('''SELECT sell_price FROM goods_in_different_airport 
                              WHERE airport_ident = %s AND goods_id = %s''', (current_airport, goods_id,))
            sell_price = cursor.fetchone()[0]
            total_revenue = quantity * sell_price

            # update player funds
            cursor.execute("UPDATE game SET current_funds = current_funds + %s WHERE player_id = %s",
                           (total_revenue, player_id,))
            # update the quantity of player inventory
            cursor.execute(
                "UPDATE player_inventory SET quantity = quantity - %s WHERE player_id = %s AND goods_id = %s",
                (quantity, player_id, goods_id,))
            # Remove goods with zero inventory
            cursor.execute("DELETE FROM player_inventory WHERE quantity = 0 AND player_id = %s AND goods_id = %s",
                           (player_id, goods_id))
            connection.commit()
            print(f"Successfully sold {quantity} units of goods, revenue: {total_revenue}.")
        else:
            print("Insufficient inventory to sell.")
    except Exception as e:
        return False


sell_goods(1)
