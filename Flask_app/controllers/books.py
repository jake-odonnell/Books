from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app import app
from flask import redirect, render_template, request
from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/books')
def r_books():
    books = Book.get_all()
    return render_template('books.html', books = books)

@app.route('/books/<id>')
def r_book_show(id):
    data = {
        'id': id
    }
    book = Book.get_from_id(data)
    fav_authors = Author.get_favorited(data)
    all_authors = Author.get_all()
    authors = []
    print(len(all_authors))
    for i in range(0,len(all_authors)):
        is_match = False
        for author in fav_authors:
            if author.id == all_authors[i].id:
                is_match = True
        if is_match == False:
            authors.append(all_authors[i])
    return render_template('book_show.html', all_authors = authors, authors = fav_authors, book = book)

@app.route('/add-favorited', methods = ['POST'])
def f_add_favorited():
    print(request.form)
    query = 'INSERT INTO favorites (author_id,book_id) VALUES (%(author)s, %(book)s);'
    connectToMySQL('books').query_db(query, request.form)
    id = request.form['book']
    return redirect('books/' + id)

@app.route('/add-book', methods = ['POST'])
def f_add_book():
    Book.add_book(request.form)
    return redirect('/books')