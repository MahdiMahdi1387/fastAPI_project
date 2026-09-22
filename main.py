from fastapi_offline import FastAPIOffline
from fastapi import Body
import db_control as db


app = FastAPIOffline()


@app.get('/movie/by_id')
def get_movie_by_id(movie_id: int) -> dict:
    return { 'data' : db.get_record_by_id(movie_id) }


@app.get('/movie/by_name')
def movie_by_name(title: str) -> dict:
    return { 'data' : db.get_record_by_name(title) }


@app.post('/movie/add')
def movie_additon(movie_id: int, title: str, year: int,
               imdb_rating: float, country: str, image: str | None=None) -> dict:
    is_done: bool = db.add_record(movie_id, title, year, imdb_rating, country, image)

    return { 'status_bool' : is_done }


@app.put('/movie/update')
def update_movie(movie_id: int, fields: dict=Body(...)) -> dict:
    if not fields:
        return { 'status_bool' : False }
    
    is_done: bool = db.update_record(movie_id, **fields)

    return { 'status_bool' : is_done }


@app.delete('/movie/delete')
def movie_delete(movie_id: int) -> dict:
    is_done: bool = db.delete_record(movie_id)

    return { 'status_bool' : is_done }


@app.get('/movie/is_in_db')
def movie_check(movie_id: int) -> bool:
    return { 'data' : db.is_in_db(movie_id) }
