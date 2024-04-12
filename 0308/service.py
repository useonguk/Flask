from model import TodoList
from db import TodoDB

class TodoService:
    def __init__(self):
        self.todo_list = TodoList()
        self.todo_db = TodoDB()
        
    def get_tasks(self):
        return self.todo_list.get_tasks()
    
    def add_task(self, task):
        self.todo_list.add_task(task)
        
    def delete_task(self, index) :
        self.todo_list.delete_task(index)
        
    def com_task(self, index):
        self.todo_list.com_task(index)