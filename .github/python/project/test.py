# from geopy import distance
# import mariadb
# import sys
#
# try:
#     conn = mariadb.connect(
#         user="root",
#         password="19990324s",
#         host="127.0.0.1",
#         port=3306,
#         database="flight_game"
#
#     )
# except mariadb.Error as e:
#     print(f"Error connecting to MariaDB Platform: {e}")
#     sys.exit(1)


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
import sqlite3
import pandas as pd

# 读取CSV文件数据
airports_file = 'filtered_airports.csv'  # 您提供的机场数据文件
products_file = 'products.csv'  # 您提供的商品列表文件
stock_file = 'limited_airport_trade_game.csv'  # 机场商品存量表

# 读取 CSV 数据到 DataFrame
airports_df = pd.read_csv(airports_file)
products_df = pd.read_csv(products_file)
stock_df = pd.read_csv(stock_file)

# 初始化数据库连接
conn = sqlite3.connect('trade_game.db')
cursor = conn.cursor()

# 创建数据库表
def initialize_database():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Airports (
                        airport_id INTEGER PRIMARY KEY,
                        name TEXT,
                        city TEXT,
                        region TEXT,
                        latitude REAL,
                        longitude REAL,
                        country TEXT,
                        iata_code TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                        product_id INTEGER PRIMARY KEY,
                        name TEXT,
                        category TEXT,
                        base_price INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Airport_Stock (
                        airport_id INTEGER,
                        product_id INTEGER,
                        buy_price INTEGER,
                        sell_price INTEGER,
                        stock INTEGER,
                        refresh_day INTEGER,
                        PRIMARY KEY (airport_id, product_id),
                        FOREIGN KEY (airport_id) REFERENCES Airports(airport_id),
                        FOREIGN KEY (product_id) REFERENCES Products(product_id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Player_Info (
                        player_id INTEGER PRIMARY KEY,
                        name TEXT,
                        current_funds INTEGER,
                        current_airport INTEGER,
                        current_day INTEGER,
                        FOREIGN KEY (current_airport) REFERENCES Airports(airport_id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Player_Inventory (
                        player_id INTEGER,
                        product_id INTEGER,
                        quantity INTEGER,
                        buy_price INTEGER,
                        PRIMARY KEY (player_id, product_id),
                        FOREIGN KEY (player_id) REFERENCES Player_Info(player_id),
                        FOREIGN KEY (product_id) REFERENCES Products(product_id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Transaction_Log (
                        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        player_id INTEGER,
                        action TEXT,
                        airport_id INTEGER,
                        product_id INTEGER,
                        quantity INTEGER,
                        price INTEGER,
                        total_amount INTEGER,
                        transaction_day INTEGER,
                        FOREIGN KEY (player_id) REFERENCES Player_Info(player_id),
                        FOREIGN KEY (airport_id) REFERENCES Airports(airport_id),
                        FOREIGN KEY (product_id) REFERENCES Products(product_id))''')
    conn.commit()

# 插入数据到数据库
def insert_data():
    # 插入机场数据
    for index, row in airports_df.iterrows():
        cursor.execute('''INSERT OR IGNORE INTO Airports (airport_id, name, city, region, latitude, longitude, country, iata_code) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (index, row['name'], row['municipality'], row['iso_region'], row['latitude_deg'],
                        row['longitude_deg'], row['iso_country'], row['ident']))

    # 插入商品数据
    for _, row in products_df.iterrows():
        cursor.execute('''INSERT OR IGNORE INTO Products (product_id, name, category, base_price) 
                          VALUES (?, ?, ?, ?)''',
                       (row['id'], row['name'], "General", 0))  # 暂时设定商品类别为"General"

    # 插入机场商品库存数据
    for _, row in stock_df.iterrows():
        cursor.execute('''INSERT OR IGNORE INTO Airport_Stock (airport_id, product_id, buy_price, sell_price, stock, refresh_day) 
                          VALUES (?, ?, ?, ?, ?, ?)''',
                       (row['airport_ident'], row['product_id'], row['buy_price'], row['sell_price'], row['stock'], 7))
    conn.commit()

# 玩家初始化
def player_setup():
    cursor.execute("SELECT airport_id, name FROM Airports")
    airports = cursor.fetchall()
    print("选择您的初始机场：")
    for airport in airports:
        print(f"{airport[0]}. {airport[1]}")

    start_airport = int(input("输入机场编号: "))
    player_name = input("输入您的玩家名称: ")

    cursor.execute("INSERT INTO Player_Info (player_id, name, current_funds, current_airport, current_day) VALUES (1, ?, 10000, ?, 0)",
                   (player_name, start_airport))
    conn.commit()

# 查看目标机场商品
def view_airport_stock(airport_id):
    cursor.execute('''SELECT p.name, s.buy_price, s.sell_price, s.stock
                      FROM Airport_Stock s
                      JOIN Products p ON s.product_id = p.product_id
                      WHERE s.airport_id = ?''', (airport_id,))
    products = cursor.fetchall()
    if products:
        print(f"\n目标机场 {airport_id} 的商品列表：")
        for product in products:
            print(f"商品: {product[0]}, 买价: {product[1]}, 卖价: {product[2]}, 库存: {product[3]}")
    else:
        print("该机场没有可用商品。")

# 购买商品
def buy_product():
    cursor.execute("SELECT current_airport, current_funds FROM Player_Info WHERE player_id = 1")
    current_airport, current_funds = cursor.fetchone()

    view_airport_stock(current_airport)

    product_id = int(input("输入要购买的商品编号: "))
    quantity = int(input("输入购买数量: "))

    cursor.execute('''SELECT buy_price, stock FROM Airport_Stock WHERE airport_id = ? AND product_id = ?''',
                   (current_airport, product_id))
    product = cursor.fetchone()

    if product and quantity <= product[1]:
        total_cost = product[0] * quantity
        if total_cost <= current_funds:
            # 更新玩家资金
            cursor.execute("UPDATE Player_Info SET current_funds = current_funds - ? WHERE player_id = 1", (total_cost,))
            # 更新库存
            cursor.execute('''UPDATE Airport_Stock SET stock = stock - ? WHERE airport_id = ? AND product_id = ?''',
                           (quantity, current_airport, product_id))
            # 更新玩家背包
            cursor.execute('''INSERT OR IGNORE INTO Player_Inventory (player_id, product_id, quantity, buy_price)
                              VALUES (1, ?, ?, ?)''', (product_id, quantity, product[0]))
            cursor.execute('''UPDATE Player_Inventory SET quantity = quantity + ? WHERE player_id = 1 AND product_id = ?''',
                           (quantity, product_id))
            conn.commit()
            print(f"成功购买 {quantity} 单位商品（总计花费: {total_cost}）。")
        else:
            print("资金不足，无法购买。")
    else:
        print("库存不足或商品不存在。")

# 主游戏逻辑
def main_game():
    print("欢迎来到贸易模拟游戏！")
    initialize_database()
    insert_data()
    player_setup()

    # 游戏菜单循环
    while True:
        print("\n=== 操作菜单 ===")
        print("1. 查看当前机场商品")
        print("2. 查看目标机场商品")
        print("3. 购买商品")
        print("4. 卖出商品")
        print("5. 移动到其他机场")
        print("6. 查看玩家状态")
        print("7. 退出游戏")

        choice = input("选择操作: ")

        if choice == '1':
            cursor.execute("SELECT current_airport FROM Player_Info WHERE player_id = 1")
            current_airport = cursor.fetchone()[0]
            view_airport_stock(current_airport)

        elif choice == '3':
            buy_product()

# 启动游戏
main_game()


# 卖出商品
def sell_product():
    cursor.execute("SELECT current_airport FROM Player_Info WHERE player_id = 1")
    current_airport = cursor.fetchone()[0]

    # 查看玩家库存
    cursor.execute('''SELECT p.name, i.quantity, i.buy_price, p.product_id
                      FROM Player_Inventory i
                      JOIN Products p ON i.product_id = p.product_id
                      WHERE i.player_id = 1''')
    inventory = cursor.fetchall()

    if not inventory:
        print("您没有任何库存可供卖出。")
        return

    print("\n您的库存：")
    for item in inventory:
        print(f"商品: {item[0]}, 数量: {item[1]}, 购入价: {item[2]}")

    product_id = int(input("输入要卖出的商品编号: "))
    quantity = int(input("输入卖出数量: "))

    # 检查库存是否足够
    cursor.execute('''SELECT quantity FROM Player_Inventory WHERE player_id = 1 AND product_id = ?''', (product_id,))
    stock = cursor.fetchone()
    if stock and quantity <= stock[0]:
        # 获取目标商品在当前机场的卖价
        cursor.execute('''SELECT sell_price FROM Airport_Stock WHERE airport_id = ? AND product_id = ?''',
                       (current_airport, product_id))
        sell_price = cursor.fetchone()[0]

        # 计算卖出总额
        total_revenue = quantity * sell_price

        # 更新玩家资金
        cursor.execute("UPDATE Player_Info SET current_funds = current_funds + ? WHERE player_id = 1", (total_revenue,))

        # 更新玩家库存
        cursor.execute('''UPDATE Player_Inventory SET quantity = quantity - ? WHERE player_id = 1 AND product_id = ?''',
                       (quantity, product_id))

        # 移除库存为零的商品
        cursor.execute("DELETE FROM Player_Inventory WHERE quantity = 0 AND player_id = 1 AND product_id = ?",
                       (product_id,))

        conn.commit()
        print(f"成功卖出 {quantity} 单位商品，收入: {total_revenue}。")
    else:
        print("库存不足，无法卖出。")


# 移动到其他机场
def move_to_airport():
    cursor.execute("SELECT airport_id, name FROM Airports")
    airports = cursor.fetchall()
    print("\n可移动的机场列表：")
    for airport in airports:
        print(f"{airport[0]}. {airport[1]}")

    target_airport = int(input("输入目标机场编号: "))
    cursor.execute("SELECT current_day FROM Player_Info WHERE player_id = 1")
    current_day = cursor.fetchone()[0]

    # 移动消耗 0.5 天
    cursor.execute("UPDATE Player_Info SET current_airport = ?, current_day = ? WHERE player_id = 1",
                   (target_airport, current_day + 0.5))
    conn.commit()
    print(f"成功移动到目标机场：{target_airport}")


# 库存刷新机制
def refresh_stock():
    cursor.execute("SELECT current_day FROM Player_Info WHERE player_id = 1")
    current_day = cursor.fetchone()[0]

    # 每7天刷新库存
    if current_day % 7 == 0:
        cursor.execute("UPDATE Airport_Stock SET stock = 30 WHERE stock < 30")
        conn.commit()
        print("所有机场库存已刷新。")


# 修改主游戏循环，加入新功能
def main_game():
    print("欢迎来到贸易模拟游戏！")
    initialize_database()
    insert_data()
    player_setup()

    while True:
        print("\n=== 操作菜单 ===")
        print("1. 查看当前机场商品")
        print("2. 查看目标机场商品")
        print("3. 购买商品")
        print("4. 卖出商品")
        print("5. 移动到其他机场")
        print("6. 查看玩家状态")
        print("7. 退出游戏")

        choice = input("选择操作: ")

        if choice == '1':
            cursor.execute("SELECT current_airport FROM Player_Info WHERE player_id = 1")
            current_airport = cursor.fetchone()[0]
            view_airport_stock(current_airport)

        elif choice == '2':
            target_airport = int(input("输入目标机场编号: "))
            view_airport_stock(target_airport)

        elif choice == '3':
            buy_product()

        elif choice == '4':
            sell_product()

        elif choice == '5':
            move_to_airport()

        elif choice == '6':
            cursor.execute("SELECT * FROM Player_Info WHERE player_id = 1")
            player_info = cursor.fetchone()
            print(
                f"玩家名称: {player_info[1]}, 当前资金: {player_info[2]}, 当前所在机场: {player_info[3]}, 当前游戏天数: {player_info[4]}")

        elif choice == '7':
            print("退出游戏。")
            break

        # 刷新库存
        refresh_stock()

