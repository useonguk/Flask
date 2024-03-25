import pymysql

class ShoseDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='0000', db='holy')
        self.cur = self.db.cursor()
        print("connect ok") 
        
    def getInventory(self):
        sql = """SELECT Shoes.name AS shoe_name, Shoes.brand AS brand, Inventory.size AS shoe_size, Inventory.quantity AS quantity
                FROM Inventory
                JOIN Shoes ON Inventory.shoe_id = Shoes.shoe_id
                WHERE Inventory.store_id = 2""" #바꿔끼우기
        self.cur.execute(sql)
        
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
        sql = """UPDATE Inventory   
                SET quantity = quantity + %s
                WHERE shoe_id = %s AND store_id = %s AND size = %s"""
        self.cur.execute(sql, (increase_amount, shoe_id, store_id, size))
        self.db.commit()
        
    def getShose(self):
        sql = "SELECT * FROM shoes"
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def insert_shoe(self, shoe_name, brand, size, quantity):
     # 신발과 매장 정보를 가져오는 JOIN 쿼리
        sql = """INSERT INTO Inventory (shoe_id, store_id, size, quantity) 
                SELECT Shoes.shoe_id, Stores.store_id, %s, %s
                FROM Shoes, Stores
                WHERE Shoes.name = %s AND Shoes.brand = %s AND Stores.store_id = 2"""  # 매장 ID가 2인 경우를 가정합니다.
        
        self.cur.execute(sql, (size, quantity, shoe_name, brand))
        self.db.commit()

