import os
from typing import Optional

import models
import requests

metadata_root_url = os.environ["METADATA_API_URL"]
rating_root_url = os.environ["RATING_API_URL"]


def get_movies() -> Optional[list[models.Movie]]:
    metadata_response = requests.get(metadata_root_url)
    if metadata_response.status_code != 200:
        return None

    metadata = metadata_response.json()

    movies = []
    for item in metadata:
        metadata_id = item["id"]
        rating_response = requests.get(f"{rating_root_url}/{metadata_id}")
        if rating_response.status_code != 200:
            return None

        rating = rating_response.json()

        movies.append(
            models.Movie(
                item["id"],
                item["title"],
                item["description"],
                item["director"],
                rating["value"],
            )
        )

    return movies
