# resources/book_resource.py
from flask_restful import Resource, reqparse
from book_model import Book, db

parser = reqparse.RequestParser()
parser.add_argument('title', required=True, help="Title cannot be blank!")
parser.add_argument('author', required=True, help="Author cannot be blank!")
parser.add_argument('published_date', required=True, help="Published Date cannot be blank!")

class BookListResource(Resource):
    def get(self):
        books = Book.query.all()
        return [book.as_dict() for book in books], 200

    def post(self):
        args = parser.parse_args()
        new_book = Book(title=args['title'], author=args['author'], published_date=args['published_date'])
        db.session.add(new_book)
        db.session.commit()
        return new_book.as_dict(), 201

class BookResource(Resource):
    def get(self, book_id):
        book = Book.query.get(book_id)
        if book:
            return book.as_dict(), 200
        return {'message': 'Book not found'}, 404

    def put(self, book_id):
        args = parser.parse_args()
        book = Book.query.get(book_id)
        if book:
            book.title = args['title']
            book.author = args['author']
            book.published_date = args['published_date']
            db.session.commit()
            return {'message': 'Book updated'}, 200
        return {'message': 'Book not found'}, 404

    def delete(self, book_id):
        book = Book.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
            return {'message': 'Book deleted'}, 200
        return {'message': 'Book not found'}, 404
