class Book:
    def __init__(self, id, title, author, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.published_date = published_date

def book_to_dict(book):
    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "published_date": book.published_date,
    }

def dict_to_book(book_dict):
    return Book(
        id=book_dict["id"],
        title=book_dict["title"],
        author=book_dict["author"],
        published_date=book_dict["published_date"],
    )

books = [
    book_to_dict(Book(1, "1984", "George Orwell", "1949-06-08")),
    book_to_dict(Book(2, "To Kill a Mockingbird", "Harper Lee", "1960-07-11")),
]
