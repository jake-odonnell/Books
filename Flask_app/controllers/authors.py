from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app import app
from flask import redirect, render_template, request

@app.route('/')
def home():
    return redirect('/authors')

@app.route('/authors')
def r_home():
    authors = Author.get_all()
    return render_template('authors.html', authors = authors)

@app.route('/add-author', methods = ['POST'])
def f_new_author():
    Author.add_author(request.form)
    return redirect('/')

@app.route('/author/<id>')
def r_author_show(id):
    data = {'id': id}
    fav_books = Book.get_favs(data)
    all_books = Book.get_all()
    return render_template('author_show.html', fav_books = fav_books, all_books = all_books, author_id = id)

@app.route('/add-favorite', methods = ['POST'])
def f_add_favorite():
    print(request.form)
    query = 'INSERT INTO favorites (author_id,book_id) VALUES (%(author)s, %(book)s);'
    connectToMySQL('books').query_db(query, request.form)
    id = request.form['author_id']
    return redirect('author/' + id)