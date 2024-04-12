from models.model import RestDB

class RestService:
    
    def __init__(self):
        self.rest_db = RestDB()
        
    def get_rest_name(self):
        return self.rest_db.get_rest_name()
    
    def post_rest(self, rest) :
        self.rest_db.post_ret(rest)
        
    def get_reservation(self):
        return self.rest_db.get_reservation()
    
    def delete(self, id) :
        self.rest_db.delete(id)