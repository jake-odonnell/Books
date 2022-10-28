from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app import app
from flask import redirect, render_template

@app.route('/books')
def r_books():
    books = Book.get_all()
    return render_template('books.html', books = books)

@app.route('/books/<id>')
def r_book_show(id):
    authors = Author.get_favorited({'id':id})
    pass