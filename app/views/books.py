from flask import Blueprint, render_template
from app.models.Book import Book

bp = Blueprint("books", __name__, url_prefix="/books")


@bp.route("/")
def list():
    books = Book.query.all()
    return render_template("books/list.html", books=books)


# TODO: add profile editing
