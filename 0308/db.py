import pymysql

class TodoDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='0000', db='start')
        self.cur = self.db.cursor()
        print("connect ok")
        
    def add(self, task) :
        sql = "INSERT INTO start(task) VALUES ('{0}')".format(task['name'])
        # self.sqlStart(sql)
        self.cur.execute(sql)
        self.db.commit()
    
    # def sqlStart(self, sql):
    #     self.cur.execute(sql)
    #     self.db.commit()
    
  
