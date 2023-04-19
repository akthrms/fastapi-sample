from dataclasses import dataclass


@dataclass
class Movie:
    id: int
    title: str
    description: str
    director: str
    rating: float
