from pydantic import BaseModel


class PutRatingRequest(BaseModel):
    metadata_id: int
    value: int


class GetRatingResponse(BaseModel):
    value: float
