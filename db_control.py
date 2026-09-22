import sqlite3 as sq
from logging import getLogger


logger = getLogger(__name__)
DB_NAME = '/home/mahdi/Desktop/fastapi_project/src/movies.db'


def init() -> None:
    """Initializes the database."""

    conn = sq.connect(DB_NAME)
    cursor = conn.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            year INTEGER NOT NULL,
            imdb_rating REAL NOT NULL,
            country TEXT NOT NULL,
            image TEXT
        )
    """
    cursor.execute(query)
    conn.close()


def get_record_by_id(movie_id: int) -> dict | None:
    """Searchs for the record in the database by id and returns it."""

    conn = sq.connect(DB_NAME)
    conn.row_factory = sq.Row
    cursor = conn.cursor()
    query = 'SELECT * FROM movies WHERE id = ?'

    try:
        record = cursor.execute(query, (movie_id,)).fetchone()

        return dict(record) if record else None
    except Exception as e:
        logger.error(f'Error: {e}')
    finally:
        conn.close()

def get_record_by_name(title: str) -> dict | None:
    """Searchs for the record in the database by title and returns it."""

    conn = sq.connect(DB_NAME)
    conn.row_factory = sq.Row
    cursor = conn.cursor()
    query = 'SELECT * FROM movies WHERE title LIKE ? LIMIT 1'

    try:
        record = cursor.execute(query, (f'%{title}%',)).fetchone()

        return dict(record) if record else None
    except Exception as e:
        logger.error(f'Error: {e}')
    finally:
        conn.close()


def is_in_db(movie_id: int) -> bool:
    """Checks that if a record is in the database or not."""

    conn = sq.connect(DB_NAME)
    cursor = conn.cursor()
    query = 'SELECT 1 FROM movies WHERE id = ?'
    try:
        record = cursor.execute(query, (movie_id,)).fetchone()

        if record:
            return True
        else:
            return False
    except Exception as e:
        logger.error(f'Error: {e}')

        return False
    finally:
        conn.close()


def add_record(movie_id: int, title: str, year: int,
               imdb_rating: float, country: str, image: str | None=None) -> bool:
    """Adds a record to the databse."""

    conn = sq.connect(DB_NAME)
    cursor = conn.cursor()
    query = """
        INSERT INTO
        movies(id, title, year, imdb_rating, country, image)
        VALUES(?, ?, ?, ?, ?, ?)
    """

    try:
        cursor.execute(query, (movie_id, title, year,
                                        imdb_rating, country, image))
        conn.commit()

        return cursor.rowcount > 0
    except Exception as e:
        logger.error(f'Error: {e}')
        return False
    finally:
        conn.close()

def update_record(movie_id: int, **fields) -> bool:
    """Updates a record in the database."""

    if not fields or 'id' in fields.keys():
        return False

    conn = sq.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        query = 'UPDATE movies SET '
        query += ', '.join(f'{field} = ?' for field in fields.keys())
        query += ' WHERE id = ?'

        cursor.execute(query, tuple(fields.values()) + (movie_id,))
        conn.commit()

        return cursor.rowcount > 0
    except Exception as e:
        logger.error(f'Error: {e}')

        return False
    finally:
        conn.close()


def delete_record(movie_id: int) -> bool:
    """Deletes a record in the database"""

    conn = sq.connect(DB_NAME)
    cursor = conn.cursor()
    query = 'DELETE FROM movies WHERE id = ?'

    try:
        cursor.execute(query, (movie_id,))
        conn.commit()

        return cursor.rowcount > 0
    except Exception as e:
        logger.error(f'Error: {e}')

        return False
    finally:
        conn.close()


if __name__ == '__main__':
    pass