from fastapi import FastAPI

app = FastAPI()

MOVIES = [
    {"title": "Inception", "director": "Christopher Nolan", "genre": "sci-fi"},
    {"title": "The Shawshank Redemption", "director": "Frank Darabont", "genre": "drama"},
    {"title": "The Dark Knight", "director": "Christopher Nolan", "genre": "action"},
    {"title": "Pulp Fiction", "director": "Quentin Tarantino", "genre": "crime"},
    {"title": "Parasite", "director": "Bong Joon-ho", "genre": "drama"}
]
# impementing crud 0perati0ns in it for movies
@app.get('/movies/')
async def read_movies():
    return MOVIES

@app.get('/movies/ {movie_title}')
async def create_movie(movie_title: str):
    for movie in MOVIES:
        if movie.get("title").casefold == movie_title.casefold:
            return movie
        
    return {"error": "Movie not found"}

@app.get('/movies/')
async def read_movies_by_genre(genre: str):
    movies_to_return = []
    for movie in MOVIES:
        if movie.get('genre').casefold() == genre.casefold():
            movies_to_return.append(movie)
    return movies_to_return if movies_to_return else {"message": "No movies found in this genre"}

from fastapi import Body
@app.post('/movies/create_movie')
async def create_movie(new_movie = Body()):
    MOVIES.append(new_movie)
    return MOVIES

@app.put('/movies/update_movie')
async def update_movie(updated_movie=Body()):
    for i in range(len(MOVIES)):
        if MOVIES[i].get('title').casefold() == updated_movie.get('title').casefold():
            MOVIES[i] = updated_movie
            return {"message": "Movie updated successfully"}
    return {"error": "Movie not found"}

@app.delete('/movies/delete_movie/{movie_title}')
async def delete_movie(movie_title: str):
    for i in range(len(MOVIES)):
        if MOVIES[i].get('title').casefold() == movie_title.casefold():
            deleted_movie = MOVIES.pop(i)
            return {"message": "Movie deleted successfully", "deleted_movie": deleted_movie}
    return {"error": "Movie not found"}

# Visit http://127.0.0.1:8000/docs to see the interactive Swagger UI documentation.
