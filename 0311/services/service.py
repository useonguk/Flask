from models.db import PostDB

class PostService:
    
    def __init__(self):
        self.post_db = PostDB()
        
    def get_tasks(self):
        return self.post_db.get()  # PostDB 인스턴스의 get 메서드를 호출해야 합니다.
    
    def add_task(self, task):
        self.post_db.add(task)  # PostDB 인스턴스의 add 메서드를 호출해야 합니다.
       
    def updata_tasks(self, task) :
        self.post_db.update(task)
        
    def delete_tasks(self, task):
        self.post_db.delete(task)
    
    def get(self, task) :
        return self.post_db.get_up(task)
        
    # def delete_task(self, index) :
    #     self.todo_list.delete_task(index)
        
    # def com_task(self, index):
        # self.todo_list.com_task(index)
        
        
# result = self.cur.fetchall()
# return result

# result = self.cur.fetchone()
# return result