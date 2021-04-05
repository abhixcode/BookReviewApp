from flask import render_template, url_for, flash, redirect, request, Blueprint
from bookreview.readinglist.forms import ListForm, SearchnaddForm, SearchForm
from bookreview.models import User, Readinglist
from bookreview import create_app,db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import requests
import json

readinglist = Blueprint('readinglist', __name__)

# Home page functionality that lists all the current reviews by the user
@readinglist.route('/list')
@readinglist.route('/')
@login_required
def home():
    user = User.query.filter_by(id=current_user.id).first_or_404()
    readinglist = Readinglist.query.filter_by(author=user).all()
    return render_template("books.html", readinglist=readinglist, title = "Bookhead")

# Functionality to add a new review by the user
@readinglist.route("/list/new", methods=['GET', 'POST'])
@login_required
def new_list():
    form = ListForm()
    if form.validate_on_submit():
        alist = Readinglist(bookname=form.bookname.data, review = form.review.data, 
            isbn = form.isbn.data,libid = form.libraryid.data,author=current_user)       
        db.session.add(alist)
        db.session.commit()
        flash('Your list has been created!', 'success')
        return redirect(url_for('readinglist.home',user_id=current_user.id))
    return render_template('create_list.html', title='New List',
                           form=form, legend='New List')

# Functionality view a particular review
@readinglist.route("/book/<int:list_id>")
@login_required
def alist(list_id):
    alist = Readinglist.query.get_or_404(list_id)
    return render_template('alist.html', title=alist.bookname, alist=alist)

# Functionality to update a review
@readinglist.route("/book/<int:list_id>/update", methods=['GET', 'POST'])
@login_required
def update_list(list_id):
    readinglist = Readinglist.query.get_or_404(list_id)
    if readinglist.author != current_user:
        abort(403)
    form = ListForm()
    if form.validate_on_submit():
        readinglist.bookname = form.bookname.data
        readinglist.review = form.review.data
        readinglist.isbn = form.isbn.data
        readinglist.libid = form.libraryid.data
        db.session.commit()
        flash('Your review has been updated!', 'success')
        return redirect(url_for('readinglist.home',user_id=current_user.id))
    elif request.method == 'GET':
        form.bookname.data = readinglist.bookname
        form.review.data = readinglist.review
        form.isbn.data = readinglist.isbn
        form.libraryid.data = readinglist.libid
    return render_template('create_list.html', title='Update List',
                           form=form, legend='Update List')

# Functionality to delete a review
@readinglist.route("/book/<int:list_id>/delete", methods=['POST'])
@login_required
def delete_list(list_id):
    readinglist = Readinglist.query.get_or_404(list_id)
    if readinglist.author != current_user:
        abort(403)
    db.session.delete(readinglist)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('readinglist.home',user_id=current_user.id))

# Functionality to add a book review
#@readinglist.route("/book/<int:list_id>/add")
#def addbook(list_id):
    #alist = Readinglist.query.get_or_404(list_id)
#    booklist = ["abcbook","1234book"]
#    return render_template('addbook.html', title='abc', booklist=booklist)

# Functionality to search a book from external API
@readinglist.route("/book/<bookname>/search",methods=['GET', 'POST'])
def booknamesearch(bookname):
    form = SearchnaddForm()
    if form.validate_on_submit():
        alist = Readinglist(bookname=form.bookname.data, review = form.review.data, 
            isbn = form.isbn.data,libid = form.libraryid.data,author=current_user)        
        db.session.add(alist)
        db.session.commit()
        flash('Your list has been created!', 'success')
        return redirect(url_for('readinglist.home',user_id=current_user.id))
    response_book = requests.get("http://openlibrary.org/search.json?title="+bookname)
    json_response = response_book.json()
    docs = json_response["docs"]
    booklist = []
    for line in docs:
        if "isbn" in line and "lending_edition_s" in line :
            booklist.append(line["title"])
            booklist.append(line["isbn"][0])
            booklist.append(line["lending_edition_s"])        
    lngthoflist = len(booklist)
    return render_template("addbook.html", booklist=booklist, lngthoflist = lngthoflist, title = "Add Book",form=form)

# Functionality to add a book review after searching
@readinglist.route("/list/search", methods=['GET', 'POST'])
@login_required
def searchbook():
    form = SearchForm()
    if form.validate_on_submit():
        bookname = form.bookname.data,
        flash('Your search results below', 'success')
        return redirect(url_for('readinglist.booknamesearch',bookname=bookname))
    return render_template('searchbook.html', title='New List',
                           form=form, legend='New List')

