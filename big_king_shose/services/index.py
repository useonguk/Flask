from model.index import ShoseDB

shose_db = ShoseDB()

class ShoseService :
    def __init__(self):
        self.shose_db = ShoseDB()
        
    def getInventory(self):
        return self.shose_db.getInventory()
    
    def decrease_inventory(self, id, store, size):
        return self.shose_db.decrease_inventory(id, store, size)
    
    def increase_inventory(self, id, store, size, increase_amount):
        self.shose_db.increase_inventory(id, store, size, increase_amount)
        
    def get_shose(self):
        return self.shose_db.getShose()
    
    def insert_shoe(self, shoe_name, brand, size, quantity):
        self.shose_db.insert_shoe(shoe_name, brand, size, quantity)