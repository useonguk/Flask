import pymysql
from flask import jsonify

class ShoseDB:
    def __init__(self):
        try:
            self.db = pymysql.connect(host='localhost', user='root', password='0000', db='holy')
            self.cur = self.db.cursor()
            print("connect ok")
        except pymysql.Error as e:
            print("Error connecting to database:", e)

    def __del__(self):
        try:
            if self.cur:
                self.cur.close()
            if self.db:
                self.db.close()
        except pymysql.Error as e:
            print("Error closing database connection:", e)

    def getInventory(self, id):
        try:
            sql = """SELECT Shoes.name AS shoe_name, Shoes.brand AS brand, Inventory.size AS shoe_size, Inventory.quantity AS quantity
                    FROM Inventory
                    JOIN Shoes ON Inventory.shoe_id = Shoes.shoe_id
                    WHERE Inventory.store_id = %s"""
            self.cur.execute(sql, (id,))
            columns = [column[0] for column in self.cur.description]
            results = [dict(zip(columns, row)) for row in self.cur.fetchall()]
            return results
        except pymysql.Error as e:
            print("Error executing query:", e)
            return []

    def decrease_inventory(self, shoe_id, store_id, size):
        try:
            sql = """UPDATE Inventory 
                    SET quantity = quantity - 1
                    WHERE shoe_id = %s AND store_id = %s AND size = %s"""
            self.cur.execute(sql, (shoe_id, store_id, size))
            self.db.commit()
        except pymysql.Error as e:
            print("Error updating inventory:", e)

    def increase_inventory(self, shoe_id, store_id, size, increase_amount):
        try:
            self.cur.execute("SELECT * FROM Inventory WHERE shoe_id = %s AND store_id = %s AND size = %s", (shoe_id, store_id, size))
            existing_data = self.cur.fetchone()

            if existing_data:
                new_quantity = existing_data[3] + increase_amount
                self.cur.execute("UPDATE Inventory SET quantity = %s WHERE shoe_id = %s AND store_id = %s AND size = %s", (new_quantity, shoe_id, store_id, size))
                self.db.commit()
                return jsonify({"message": "Inventory updated successfully."})
            else:
                self.cur.execute("INSERT INTO Inventory (shoe_id, store_id, size, quantity) VALUES (%s, %s, %s, %s)", (shoe_id, store_id, size, increase_amount))
                self.db.commit()
                return jsonify({"message": "New inventory added successfully."})
        except pymysql.Error as e:
            print("Error updating inventory:", e)

    def getShose(self):
        try:
            sql = "SELECT * FROM shoes"
            self.cur.execute(sql)
            return self.cur.fetchall()
        except pymysql.Error as e:
            print("Error executing query:", e)
            return []

    def insert_shoe(self, shoe_name, brand, size, quantity):
        try:
            sql = """INSERT INTO Inventory (shoe_id, store_id, size, quantity) 
                    SELECT Shoes.shoe_id, Stores.store_id, %s, %s
                    FROM Shoes, Stores
                    WHERE Shoes.sname = %s AND Shoes.brand = %s AND Stores.store_id = 2"""
            self.cur.execute(sql, (size, quantity, shoe_name, brand))
            self.db.commit()
        except pymysql.Error as e:
            print("Error inserting shoe:", e)

    def getStore(self):
        try:
            sql = "SELECT * FROM Store"
            self.cur.execute(sql)
            return self.cur.fetchall()
        except pymysql.Error as e:
            print("Error executing query:", e)
            return []

    def postShose(self, name, brand):
        try:
            sql_check = """SELECT COUNT(*) FROM Shoes WHERE name = %s AND brand = %s"""
            self.cur.execute(sql_check, (name, brand))
            result = self.cur.fetchone()

            if result[0] > 0:
                return {"error": "Duplicate entry"}, 409
            else:
                sql_duplicate_check = """SELECT COUNT(*) FROM Shoes WHERE name = %s OR brand = %s"""
                self.cur.execute(sql_duplicate_check, (name, brand))
                duplicate_result = self.cur.fetchone()
                if duplicate_result[0] == 0:
                    sql_insert = """INSERT INTO Shoes (name, brand) VALUES (%s, %s)"""
                    self.cur.execute(sql_insert, (name, brand))
                    self.db.commit()
                    return {"message": "Shoe added successfully"}, 201
                else:
                    return {"error": "Shoe with the same name and brand already exists"}, 409
        except pymysql.Error as e:
            print("Error posting shoe:", e)

    def getStore(self):
        try:
            sql = "SELECT * FROM Store"
            self.cur.execute(sql)
            return self.cur.fetchall()
        except pymysql.Error as e:
            print("Error executing query:", e)
            # 여기서 데이터베이스 연결을 재시도할 수 있습니다.
            # 또는 다른 예외 처리 로직을 추가할 수도 있습니다.
            return [{e}]
        except AttributeError as e:
            print("Attribute error:", e)
            # 데이터베이스 연결을 다시 설정하는 등의 작업을 수행할 수 있습니다.
            # 예를 들어, self.__init__()을 호출하여 새로운 연결을 설정할 수 있습니다.
            
            return [{e}]

