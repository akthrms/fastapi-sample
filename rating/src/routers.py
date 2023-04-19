import cruds
import gateways
import schemas
from fastapi import APIRouter, HTTPException, Response

router = APIRouter()


@router.get("/rating/{metadata_id}", response_model=schemas.RatingResponse)
def get_rating(metadata_id: int) -> schemas.RatingResponse:
    if not gateways.exists_movie(metadata_id):
        raise HTTPException(404, "metadata not found")

    ratings = cruds.get_ratings(metadata_id)
    values = [rating.value for rating in ratings]
    return schemas.RatingResponse(
        value=0.0 if len(ratings) == 0 else (sum(values) / len(values))
    )


@router.post("/rating")
def post_rating(rating: schemas.RatingRequest) -> Response:
    if not gateways.exists_movie(rating.metadata_id):
        raise HTTPException(404, "metadata not found")

    cruds.post_rating(rating.metadata_id, rating.value)
    return Response(status_code=200)
