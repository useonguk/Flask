class TodoList:
    def __init__(self):
        self.tasks = []

    def get_tasks(self):
        return self.tasks
    
    def add_task(self, task) :
        self.todo_list.add_task(task)
        self.todo_db.add(task)
        
    def add_task(self, task) :
        self.tasks.append(task) 
        
    def delete_task(self, index):
        if 0 <= index < len(self.tasks) :
            del self.tasks[index]
            
    def com_task(self, index) :
        self.tasks[index]["completed"] = True
        
    