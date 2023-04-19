import gateways
import schemas
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/movie", response_model=list[schemas.MovieResponse])
def get_movies() -> list[schemas.MovieResponse]:
    movies = gateways.get_movies()
    if movies is None:
        raise HTTPException(500, "failed to get movies")

    return [
        schemas.MovieResponse(
            id=movie.id,
            title=movie.title,
            description=movie.description,
            director=movie.director,
            rating=movie.rating,
        )
        for movie in movies
    ]
