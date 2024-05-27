# Example Book API

A simple RESTful API for managing books, built with Flask and SQLAlchemy.

## Features

- Create, read, update, and delete books
- Unit tests for all endpoints

## Prerequisites

- Python 3.6+
- pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/lainceline/lain_example_api.git
   cd lain_example_api
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

1. Initialize the database:

   ```bash
   flask shell
   ```

2. In the Python shell, create the tables:

   ```python
   from app import db
   db.create_all()
   exit()
   ```

## Running the Application

1. Start the Flask development server:

   ```bash
   flask run
   ```

2. The API will be accessible at `http://127.0.0.1:5000/`.

## API Endpoints

- `GET /books`: Get a list of all books
- `POST /books`: Add a new book
- `GET /books/<int:book_id>`: Get a book by ID
- `PUT /books/<int:book_id>`: Update a book by ID
- `DELETE /books/<int:book_id>`: Delete a book by ID

## Running Unit Tests

1. Ensure you are in the virtual environment.

2. Run the tests using `unittest`:

   ```bash
   python -m unittest discover -s tests
   ```

## Project Structure

```
lain_example_api/
│
├── app.py                    # Main application file
├── book_model.py             # SQLAlchemy Book model
├── database.py               # Database operations
├── requirements.txt          # Python packages
├── resources/
│   └── book_resource.py      # API resource definitions
├── tests/
│   └── test_api.py           # Unit tests
└── README.md                 # Project documentation
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
