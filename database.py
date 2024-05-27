from book_model import books, book_to_dict, dict_to_book

def get_all_books():
    return books

def get_book_by_id(book_id):
    return next((book for book in books if book["id"] == book_id), None)

def add_book(book):
    books.append(book_to_dict(book))

def update_book(book_id, title, author, published_date):
    book = get_book_by_id(book_id)
    if book:
        book["title"] = title
        book["author"] = author
        book["published_date"] = published_date
        return True
    return False

def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
