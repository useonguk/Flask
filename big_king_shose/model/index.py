import pymysql
from flask import jsonify

class ShoseDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='0000', db='holy')
        self.cur = self.db.cursor()
        print("connect ok")

    def __del__(self):
        self.db.close()

    def getInventory(self, id):
        sql = """SELECT Shoes.name AS shoe_name, Shoes.brand AS brand, Inventory.size AS shoe_size, Inventory.quantity AS quantity
                FROM Inventory
                JOIN Shoes ON Inventory.shoe_id = Shoes.shoe_id
                WHERE Inventory.store_id = """ + str(id) #바꿔끼우기
        self.cur.execute(sql)
        return self.cur.fetchall()

        # 결과를 딕셔너리 형태로 변환하여 반환
        columns = [column[0] for column in self.cur.description]
        results = []
        for row in self.cur.fetchall():
            results.append(dict(zip(columns, row)))

        return results

    def decrease_inventory(self, shoe_id, store_id, size):
        sql = """UPDATE Inventory 
                SET quantity = quantity - 1
                WHERE shoe_id = %s AND store_id = %s AND size = %s"""
        self.cur.execute(sql, (shoe_id, store_id, size))
        self.db.commit()

    def increase_inventory(self, shoe_id, store_id, size, increase_amount):
        self.cursor.execute("SELECT * FROM Inventory WHERE shoe_id = %s AND store_id = %s AND size = %s", (shoe_id, store_id, size))
        existing_data = self.cursor.fetchone()

        if existing_data:
            # 데이터가 이미 존재하는 경우, 업데이트 수행
            new_quantity = existing_data[3] + increase_amount
            self.cursor.execute("UPDATE Inventory SET quantity = %s WHERE shoe_id = %s AND store_id = %s AND size = %s", (new_quantity, shoe_id, store_id, size))
            self.db.commit()
            return jsonify({"message": "Inventory updated successfully."})
        else:
            # 데이터가 존재하지 않는 경우, 삽입 수행
            self.cursor.execute("INSERT INTO Inventory (shoe_id, store_id, size, quantity) VALUES (%s, %s, %s, %s)", (shoe_id, store_id, size, increase_amount))
            self.db.commit()
            return jsonify({"message": "New inventory added successfully."})

    def getShose(self):
        sql = "SELECT * FROM shoes"
        self.cur.execute(sql)
        return self.cur.fetchall()

    def insert_shoe(self, shoe_name, brand, size, quantity):
        # 신발과 매장 정보를 가져오는 JOIN 쿼리
        sql = """INSERT INTO Inventory (shoe_id, store_id, size, quantity) 
                SELECT Shoes.shoe_id, Stores.store_id, %s, %s
                FROM Shoes, Stores
                WHERE Shoes.sname = %s AND Shoes.brand = %s AND Stores.store_id = 2"""  # 매장 ID가 2인 경우를 가정합니다.

        self.cur.execute(sql, (size, quantity, shoe_name, brand))
        self.db.commit()

    def getStore(self):
        sql = "SELECT * FROM Store"
        self.cur.execute(sql)
        return self.cur.fetchall()  

    
    def postShose(self, name, brand):
        sql_check = """SELECT COUNT(*) FROM Shoes WHERE name = %s AND brand = %s"""
        self.cur.execute(sql_check, (name, brand))
        result = self.cur.fetchone()

        if result[0] > 0:
            # 중복된 데이터가 있는 경우
            return {"error": "Duplicate entry"}, 409
        else:
            # 중복된 데이터가 없는 경우
            # 같은 이름과 같은 브랜드를 가진 신발이 없는 경우에만 추가
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


        
    def postStore(self, name, location):
        sql = "INSERT INTO Store (name, location) VALUES (%s, %s)"
        self.cur.execute(sql, (name, location))
        self.db.commit()
