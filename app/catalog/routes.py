from app.catalog import main
from app import db
from app. catalog.model import Book
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required


@main.route("/", methods=["GET", "POST"])
@login_required
def home():
    books = None
    if request.form:
        try:
            book = Book(title=request.form.get("title"))
            db.session.add(book)
            db.session.commit()
        except Exception as e:
            print("Failed to add book")
            print(e)
    books = Book.query.all()
    return render_template("home.html", books=books)


@main.route("/update", methods=["POST"])
@login_required
def update():
    try:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        book = Book.query.filter_by(title=oldtitle).first()
        book.title = newtitle
        db.session.commit()
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/")


@main.route("/delete", methods=["POST"])
@login_required
def delete():
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
   # return {'message': 'book delete successfully'}
   # flash('book delete successfully')
    return redirect("/")
