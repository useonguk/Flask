import pymysql   

class RestDB:
    GlvName = ""
    
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='0000', db='holy')
        self.cur = self.db.cursor()
        print("connect ok") 
    
    def get_rest_name(self):
        sql = "SELECT * FROM Restaurant"
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def post_ret(self, rest):
        RestDB.GlvName = rest.get('name')
        
        sql_check_user = "SELECT id FROM People WHERE name = %s"
        self.cur.execute(sql_check_user, (rest.get('name'),))
        existing_user = self.cur.fetchone()
        
        if existing_user :
            people_id = existing_user[0]
        else :
            sql_insert_people = "INSERT INTO People (name) VALUES (%s)"
            self.cur.execute(sql_insert_people, (rest.get('name'),))
            self.db.commit()
    
        sql_select_people_id = "SELECT id FROM People WHERE name = %s"
        self.cur.execute(sql_select_people_id, (rest.get('name'),))
        people_id = self.cur.fetchone()[0]   

        sql_insert_reservation = "INSERT INTO Reservation (name, email, phone, num_guests, date_time, restaurant_id, people_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.cur.execute(sql_insert_reservation, (rest.get('name'), rest.get('email'), rest.get('phone'), rest.get('num_guests'), rest.get('date'), rest.get('restaurant_id'), people_id))
        self.db.commit()
        
    def get_reservation(self) :
        sql = "SELECT r.id, r.name AS reservation_name, r.email, r.phone, r.num_guests, r.date_time, rs.name AS restaurant_name  FROM Reservation r  JOIN Restaurant rs ON r.restaurant_id = rs.id WHERE r.name = %s"
        self.cur.execute(sql, RestDB.GlvName)
        return self.cur.fetchall()
    
    def delete(self, id):
        sql = "DELETE FROM Reservation WHERE id = %s"
        self.cur.execute(sql, id)
        self.db.commit()