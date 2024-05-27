from flask_restful import Resource, reqparse
from book_model import Book, dict_to_book, book_to_dict
import database

parser = reqparse.RequestParser()
parser.add_argument('title', required=True, help="Title cannot be blank!")
parser.add_argument('author', required=True, help="Author cannot be blank!")
parser.add_argument('published_date', required=True, help="Published Date cannot be blank!")

class BookListResource(Resource):
    def get(self):
        books = database.get_all_books()
        return books, 200

    def post(self):
        args = parser.parse_args()
        new_book = Book(id=len(database.books) + 1, **args)
        database.add_book(new_book)
        return book_to_dict(new_book), 201

class BookResource(Resource):
    def get(self, book_id):
        book = database.get_book_by_id(book_id)
        if book:
            return book, 200
        return {'message': 'Book not found'}, 404

    def put(self, book_id):
        args = parser.parse_args()
        if database.update_book(book_id, **args):
            return {'message': 'Book updated'}, 200
        return {'message': 'Book not found'}, 404

    def delete(self, book_id):
        if database.delete_book(book_id):
            return {'message': 'Book deleted'}, 200
        return {'message': 'Book not found'}, 404
