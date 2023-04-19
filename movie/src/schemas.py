from pydantic import BaseModel


class MovieResponse(BaseModel):
    id: int
    title: str
    description: str
    director: str
    rating: float
