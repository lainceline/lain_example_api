# database.py
from book_model import db, Book

def get_all_books():
    return Book.query.all()

def get_book_by_id(book_id):
    return Book.query.get(book_id)

def add_book(book):
    db.session.add(book)
    db.session.commit()

def update_book(book_id, title, author, published_date):
    book = get_book_by_id(book_id)
    if book:
        book.title = title
        book.author = author
        book.published_date = published_date
        db.session.commit()
        return True
    return False

def delete_book(book_id):
    book = get_book_by_id(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return True
    return False
