# Project Name

Gutenberg 

### Prerequisites
- Python (3.7+)
- Django (4.0)
- Django Rest Framework (3.14)

### Database Setup
- Dump the a PostgreSQL database.

## Installation
- Clone the Repository
- Create Virtual environmrnt
- Install requirements.txt using ``` pip install -r requirements.txt ```
- Run the server using ``` python manage.py runserver ```


### Access the API
- Open a web browser or use a tool like Postman to access the API endpoints.


### Example API Queries
- Example 1: Retrieve books with pagination:
    - http://127.0.0.1:8000/book/list/?page=1

- Example 2: Filter by Language and Author with Pagination:
    - http://127.0.0.1:8000/book/list/?language=en&author=United States&page=1

- Example 3: Filter by Language and Bookshelf with Pagination:
    - http://127.0.0.1:8000/book/list/?language=en&bookshelf=United States&page=1

- Example 4: Filter by Language and Mime Type with Pagination:
    - http://127.0.0.1:8000/book/list/?language=en&mime_type=text/plain&page=1

- Example 1: Filter by Book id:
    - http://127.0.0.1:8000/book/list/?book_id=2



## Note:
- Adjust the query parameters (`book_id`, `title`, `language`, `author`, `topic`, `mime_type`, `page`) according to your filtering requirements.

