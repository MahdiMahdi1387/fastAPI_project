import requests as rq


def get_movie_by_id(movie_id: int) -> tuple | str:
    """Searchs for the record in the API by id and returns it."""

    url = 'http://127.0.0.1:8000/movie/by_id'
    param = {
        'movie_id' : movie_id
    }

    response = rq.get(url, params=param)

    if response.status_code != 200:
        return 'ERROR'

    response = response.json()['data']

    title: str = response['title']
    year: int = int(response['year'])
    imdb_rating: float = float(response['imdb_rating'])
    country: str = response['country']
    image: str | None = response['image']

    return (movie_id, title, year, imdb_rating, country, image)


def get_movie_by_name(title_in: str) -> tuple | str:
    """Searchs for the record in the API by title and returns it."""

    url = 'http://127.0.0.1:8000/movie/by_name'
    param = {
        'title' : title_in
    }

    response = rq.get(url, params=param)

    if response.status_code != 200:
        return 'ERROR'

    response = response.json()['data']

    title_out: str = response['title']
    movie_id: int = int(response['id'])
    year: int = int(response['year'])
    imdb_rating: float = float(response['imdb_rating'])
    country: str = response['country']
    image: str | None = response['image']

    return (movie_id, title_out, year, imdb_rating, country, image)


def add_movie(movie_id: int, title: str, year: int,
               imdb_rating: float,
                 country: str, image: str | None=None) -> bool | str:
    """Adds a record to API's database."""

    url = 'http://127.0.0.1:8000/movie/add'
    param = {
        'movie_id' : movie_id,
        'title' : title,
        'year' : year,
        'imdb_rating' : imdb_rating,
        'country' : country,
        'image' : image
    }

    response = rq.post(url, params=param)

    if response.status_code != 200:
        return 'ERROR'

    response = response.json()['status_bool']

    return response


def update_movie(movie_id: int, title: str, year: int,
               imdb_rating: float, country: str,
                 image: str | None=None) -> bool | str:
    """Updates a record in API's database."""
    
    url = 'http://127.0.0.1:8000/movie/update'

    response = rq.put(
        url,
        params={ 'movie_id' : movie_id },
        json={
            'title' : title,
            'year' : year,
            'imdb_rating' : imdb_rating,
            'country' : country,
            'image' : image
        }
    )

    if response.status_code != 200:
        return 'ERROR'

    response = response.json()['status_bool']

    return response


def delete_movie(movie_id: int) -> bool | str:
    """Deletes a record in API's database by id."""
        
    url = 'http://127.0.0.1:8000/movie/delete'
    param = {
        'movie_id' : movie_id
    }

    response = rq.delete(url, params=param)

    if response.status_code != 200:
        return 'ERROR'

    response = response.json()['status_bool']

    return response


def check_movie(movie_id: int) -> bool | str:
    """Checks that if a record is in API's database or not."""
            
    url = 'http://127.0.0.1:8000/movie/is_in_db'
    param = {
        'movie_id' : movie_id
    }

    response = rq.get(url, params=param)

    if response.status_code != 200:
        return 'ERROR'

    return response.json()['data']


if __name__ == '__main__':
    pass
