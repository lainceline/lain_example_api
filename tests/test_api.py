import unittest
from app import app, db
from book_model import Book

class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()
            self.add_sample_books()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def add_sample_books(self):
        book1 = Book(title="1984", author="George Orwell", published_date="1949-06-08")
        book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", published_date="1960-07-11")
        db.session.add(book1)
        db.session.add(book2)
        db.session.commit()

    def test_get_books(self):
        with app.app_context():
            response = self.app.get('/books')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 2)
            self.assertEqual(response.json[0]['title'], '1984')
            self.assertEqual(response.json[1]['title'], 'To Kill a Mockingbird')

    def test_get_book(self):
        with app.app_context():
            response = self.app.get('/books/1')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['title'], '1984')

    def test_get_book_not_found(self):
        with app.app_context():
            response = self.app.get('/books/999')
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json['message'], 'Book not found')

    def test_create_book(self):
        with app.app_context():
            new_book = {
                "title": "Brave New World",
                "author": "Aldous Huxley",
                "published_date": "1932-08-18"
            }
            response = self.app.post('/books', json=new_book)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['title'], 'Brave New World')
            self.assertEqual(Book.query.count(), 3)

    def test_update_book(self):
        with app.app_context():
            updated_book = {
                "title": "1984 - Updated",
                "author": "George Orwell",
                "published_date": "1949-06-08"
            }
            response = self.app.put('/books/1', json=updated_book)
            self.assertEqual(response.status_code, 200)
            response = self.app.get('/books/1')
            self.assertEqual(response.json['title'], '1984 - Updated')

    def test_delete_book(self):
        with app.app_context():
            response = self.app.delete('/books/1')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['message'], 'Book deleted')
            self.assertEqual(Book.query.count(), 1)
            response = self.app.get('/books/1')
            self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
