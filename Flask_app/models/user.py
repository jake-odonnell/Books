

class User:
    def __init__(self, data:dict):
        self.id:int = data['id']
        self.username:str = data['username']
        self.password:str = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']