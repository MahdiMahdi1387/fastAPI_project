🎬 Movie Database API

A Python-based REST API for managing a movie database, built with FastAPI and SQLite. The project provides endpoints for retrieving, adding, updating, and deleting movie records, along with a separate Python client for interacting with the API using HTTP requests.

✨ Features

- Retrieve Movies by ID: Fetch movie information using its unique identifier.
- Search Movies by Title: Find a movie using a partial or complete title.
- Add Movies: Insert new movie records into the database.
- Update Movies: Modify existing movie information.
- Delete Movies: Remove movie records by ID.
- Check Movie Existence: Check whether a movie exists in the database.
- SQLite Integration: Store movie information in a local SQLite database.
- RESTful Architecture: Expose database operations through HTTP endpoints.
- Python API Client: Interact with the API through a separate module built with Requests.
- Basic Error Handling: Handle database operation failures and unsuccessful HTTP responses.

🛠️ Technologies Used

- Python — Application logic
- FastAPI — API framework
- SQLite — Database management
- Requests — HTTP communication between the client and API
- FastAPI Offline — Used to initialize the FastAPI application

📂 Project Structure

fastapi_project/
├── src/
│   ├── main.py
│   ├── db_control.py
│   ├── main_fastapi.py
│   └── movies.db
├── requirements.txt
└── README.md

- "main.py": Defines the API endpoints.
- "db_control.py": Implements database initialization and CRUD operations.
- "main_fastapi.py": Provides Python functions for communicating with the API.
- "movies.db": SQLite database file created or used by the application.
- "requirements.txt": Lists the project's Python dependencies.

The exact file structure may differ depending on your repository configuration.

📋 Database Schema

The application uses a "movies" table with the following columns:

Column| Type| Description
"id"| INTEGER| Unique movie identifier and primary key
"title"| TEXT| Movie title
"year"| INTEGER| Release year
"imdb_rating"| REAL| IMDb rating
"country"| TEXT| Country associated with the movie
"image"| TEXT| Optional image URL or image reference

The "title", "year", "imdb_rating", and "country" columns are required. The "image" column is optional.

⚙️ Installation

1. Clone the Repository

git clone <repository-url>
cd <repository-directory>

Replace the placeholders with your repository URL and directory name.

2. Create a Virtual Environment

python -m venv .venv

Activate it on Linux:

source .venv/bin/activate

3. Install Dependencies

If a "requirements.txt" file is available:

pip install -r requirements.txt

Otherwise, install the packages used by the application:

pip install fastapi fastapi-offline requests

The "sqlite3" and "logging" modules are included in Python's standard library.

🚀 Running the API

Start the FastAPI application from the appropriate project directory:

uvicorn main:app --reload

If your "main.py" file is inside the "src" directory and you run the command from the project root, use:

uvicorn src.main:app --reload

The application will normally be available at:

http://127.0.0.1:8000

API Documentation

FastAPI normally provides interactive API documentation at:

http://127.0.0.1:8000/docs

You can use the documentation interface to inspect endpoints and send test requests.

📡 API Endpoints

All endpoints use the "/movie" prefix.

Method| Endpoint| Description
GET| "/movie/by_id"| Retrieve a movie by ID
GET| "/movie/by_name"| Search for a movie by title
POST| "/movie/add"| Add a new movie
PUT| "/movie/update"| Update an existing movie
DELETE| "/movie/delete"| Delete a movie by ID
GET| "/movie/is_in_db"| Check whether a movie exists

1. Retrieve a Movie by ID

Request:

GET /movie/by_id?movie_id=1

Example response:

{
  "data": {
    "id": 1,
    "title": "Inception",
    "year": 2010,
    "imdb_rating": 8.8,
    "country": "USA",
    "image": null
  }
}

The example assumes that a matching record exists in the database.
GET /movie/by_name?title=Inception

The API searches for a title containing the provided text and returns at most one matching record.

3. Add a Movie

Request:

POST /movie/add?movie_id=1&title=Inception&year=2010&imdb_rating=8.8&country=USA

Example response:

{
  "status_bool": true
}

The "image" parameter is optional.

A successful insertion returns "true"; a failed database operation returns "false".

4. Update a Movie

Request:

PUT /movie/update?movie_id=1

JSON body:

{
  "title": "Inception Updated",
  "year": 2010,
  "imdb_rating": 8.9,
  "country": "USA",
  "image": null
}

Example response:

{
  "status_bool": true
}

The API updates the supplied fields for the movie with the specified ID.

5. Delete a Movie

Request:

DELETE /movie/delete?movie_id=1

Example response:

{
  "status_bool": true
}

The response indicates whether a database row was deleted.

6. Check Whether a Movie Exists

Request:

GET /movie/is_in_db?movie_id=1

Example response:

{
  "data": true
}

🐍 Python Client

The "main_fastapi.py" module provides functions for interacting with the API programmatically.

Retrieve a Movie

import main_fastapi as api

movie = api.get_movie_by_id(1)

if movie != "ERROR":
    print(movie)
else:
    print("Request failed.")

The function returns a tuple containing:

(movie_id, title, year, imdb_rating, country, image)

Search by Title

movie = api.get_movie_by_name("Inception")

Add a Movie

result = api.add_movie(
    movie_id=2,
    title="Interstellar",
    year=2014,
    imdb_rating=8.7,
    country="USA",
    image=None
)

Update a Movie

result = api.update_movie(
    movie_id=2,
    title="Interstellar",
    year=2014,
    imdb_rating=8.8,
    country="USA",
    image=None
)

Delete a Movie

result = api.delete_movie(2)

Check Whether a Movie Exists

result = api.check_movie(2)

The client functions generally return "True" or "False" for successful HTTP responses containing the expected result. They return ""ERROR"" when the HTTP status code is not "200".

🏗️ Architecture

The project separates its responsibilities into three main components:

1. API Layer: Handles HTTP requests and exposes movie-management endpoints through FastAPI.
2. Database Layer: Uses SQLite to store movie records and execute database operations.
3. Client Layer: Uses Requests to communicate with the API and provides reusable Python functions.

This separation makes the code easier to organize and provides a foundation for extending the application with additional functionality.

⚠️ Current Limitations

- The database path is currently configured as an absolute path and should be adapted to the deployment environment.
- The API does not yet use a dedicated Pydantic model for movie data validation.
- Movie searches return at most one matching record.
- The client does not currently implement explicit request timeouts.
- Error responses are relatively simple and could provide more detailed information.
- The update operation requires careful validation of field names.
- The current implementation does not include authentication or authorization.

🔮 Possible Improvements

- Add Pydantic request and response models.
- Implement pagination and multi-result searches.
- Add structured logging and more specific exception handling.
- Use environment variables or configuration files for database paths.
- Add automated tests for API endpoints and database operations.
- Improve HTTP status codes and error responses.
- Add authentication and authorization.
- Add Docker support for easier deployment.

👨‍💻 Author

Mahdi

📄 License

No license has been specified yet.
2. Search for a Movie by Title

Request:
