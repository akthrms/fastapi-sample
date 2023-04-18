import cruds
import schemas
from fastapi import APIRouter, Response

router = APIRouter()


@router.get("/rating/{metadata_id}", response_model=schemas.GetRatingResponse)
def get_rating(metadata_id: int) -> schemas.GetRatingResponse:
    ratings = cruds.get_ratings(metadata_id)
    values = [rating.value for rating in ratings]
    return schemas.GetRatingResponse(
        value=0.0 if len(ratings) == 0 else (sum(values) / len(values))
    )


@router.put("/rating")
def put_rating(rating: schemas.PutRatingRequest) -> Response:
    cruds.put_rating(rating.metadata_id, rating.value)
    return Response(status_code=200)
