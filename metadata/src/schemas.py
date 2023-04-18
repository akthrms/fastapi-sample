from pydantic import BaseModel


class GetMetadataResponse(BaseModel):
    id: int
    title: str
    description: str
    director: str
