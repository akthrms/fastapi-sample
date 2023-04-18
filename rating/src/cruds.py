import models

in_memory_store: list[models.Rating] = []


def get_ratings(metadata_id: int) -> list[models.Rating]:
    return [rating for rating in in_memory_store if rating.metadata_id == metadata_id]


def put_rating(metadata_id: int, value: int):
    in_memory_store.append(models.Rating(len(in_memory_store) + 1, metadata_id, value))
