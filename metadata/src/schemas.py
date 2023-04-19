from pydantic import BaseModel


class MetadataResponse(BaseModel):
    id: int
    title: str
    description: str
    director: str
