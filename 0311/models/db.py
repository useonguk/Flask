import pymysql   

class PostDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='0000', db='holy')
        self.cur = self.db.cursor()
        print("connect ok") 
        
    def get(self):
        sql = "SELECT * FROM testdb;"
        self.cur.execute(sql)
        return self.cur.fetchall()
        
    def add(self, task):
        sql = "INSERT INTO testDB (title, content, author) VALUES (%s, %s, %s)"
        self.cur.execute(sql, (task['title'], task['content'], task['author']))
        self.db.commit()
        
    def update(self, task) :
        sql = "UPDATE testdb SET title = %s, content = %s, author = %s WHERE id = %s" 
        self.cur.execute(sql, (task['title'], task['content'], task['author'], task['id']))
        self.db.commit()
        
    def delete(self, task) :
        sql = "DELETE FROM testdb WHERE id = %s";
        self.cur.execute(sql, (task))
        self.db.commit()
        # sql = "DELETE FROM customers WHERE age = 30";
        
    def get_up(self, task) :
        print(task)
        sql = "SELECT * FROM testdb WHERE id = %s"
        self.cur.execute(sql, (task))
        return self.cur.fetchone()