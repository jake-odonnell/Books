from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self, data:dict):
        self.id:int = data['id']
        self.name:str = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM authors'
        results = connectToMySQL('books').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @staticmethod
    def add_author(data:dict):
        query = 'INSERT INTO authors (name) VALUE(%(name)s)'
        connectToMySQL('books').query_db(query,data)
        return