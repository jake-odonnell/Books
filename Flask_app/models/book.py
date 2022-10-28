

class Book:
    def __init__(self, data:dict):
        self.id:int = data['id']
        self.title:str = data['title']
        self.num_pages:int = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    