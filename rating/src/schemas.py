from pydantic import BaseModel


class RatingRequest(BaseModel):
    metadata_id: int
    value: int


class RatingResponse(BaseModel):
    value: float
