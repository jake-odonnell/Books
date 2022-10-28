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