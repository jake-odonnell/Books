

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.config import mysqlconnection

class Book:
    def __init__(self, data:dict):
        self.id:int = data['id']
        self.title:str = data['title']
        self.num_pages:int = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM books;'
        results = connectToMySQL('books').query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def get_favs(cls, data:dict):
        query = 'SELECT * FROM books JOIN favorites ON id = favorites.book_id WHERE favorites.author_id = %(id)s;'
        results = connectToMySQL('books').query_db(query, data)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def get_from_id(cls, data:dict):
        query = 'SELECT * from books WHERE id = %(id)s;'
        result = connectToMySQL('books').query_db(query, data)
        print(result)
        book = cls(result[0])
        return book

    @classmethod
    def add_book(cls, data:dict):
        query = 'INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_pages)s);'
        id = connectToMySQL('books').query_db(query, data)
        data = {
            'id': id
        }
        return cls.get_from_id(data)