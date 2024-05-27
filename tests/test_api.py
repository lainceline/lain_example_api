import unittest
from app import app
from book_model import books, book_to_dict, Book

class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        # Reset the books list before each test
        books.clear()
        books.extend([
            book_to_dict(Book(1, "1984", "George Orwell", "1949-06-08")),
            book_to_dict(Book(2, "To Kill a Mockingbird", "Harper Lee", "1960-07-11")),
        ])

    def tearDown(self):
        # Reset the books list after each test to ensure tests are isolated
        books.clear()
        books.extend([
            book_to_dict(Book(1, "1984", "George Orwell", "1949-06-08")),
            book_to_dict(Book(2, "To Kill a Mockingbird", "Harper Lee", "1960-07-11")),
        ])

    def test_get_books(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)
        self.assertEqual(response.json[0]['title'], '1984')
        self.assertEqual(response.json[1]['title'], 'To Kill a Mockingbird')

    def test_get_book(self):
        response = self.app.get('/books/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['title'], '1984')

    def test_get_book_not_found(self):
        response = self.app.get('/books/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Book not found')

    def test_create_book(self):
        new_book = {
            "title": "Brave New World",
            "author": "Aldous Huxley",
            "published_date": "1932-08-18"
        }
        response = self.app.post('/books', json=new_book)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], 'Brave New World')
        self.assertEqual(len(books), 3)

    def test_update_book(self):
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
        response = self.app.delete('/books/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Book deleted')
        self.assertEqual(len(books), 1)
        response = self.app.get('/books/1')
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
