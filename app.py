from flask import Flask
from flask_restful import Api
from resources.book_resource import BookListResource, BookResource

app = Flask(__name__)
api = Api(app)

api.add_resource(BookListResource, '/books')
api.add_resource(BookResource, '/books/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)
