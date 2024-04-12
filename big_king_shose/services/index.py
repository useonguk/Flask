from model.index import ShoseDB

shose_db = ShoseDB()

class ShoseService :
    def __init__(self):
        self.shose_db = ShoseDB()
        
    def getInventory(self, id):
        return self.shose_db.getInventory(id)
    
    def decrease_inventory(self, id, store, size):
        return self.shose_db.decrease_inventory(id, store, size)
    
    def increase_inventory(self, id, store, size, increase_amount):
        self.shose_db.increase_inventory(id, store, size, increase_amount)
        
    def get_shose(self):
        return self.shose_db.getShose()
    
    def insert_shoe(self, shoe_name, brand, size, quantity):
        self.shose_db.insert_shoe(shoe_name, brand, size, quantity)
        
    def get_store(self):
        return self.shose_db.getStore()
    
    def post_shose(self, name, brand):
        self.shose_db.postShose(name, brand)
        
    def post_store(self, name, location):
        self.shose_db.postStore(name, location)
