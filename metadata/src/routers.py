import cruds
import schemas
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/metadata/{id}", response_model=schemas.MetadataResponse)
def get_metadata(id: int) -> schemas.MetadataResponse:
    metadata = cruds.get_metadata(id)
    if metadata is None:
        raise HTTPException(404, "metadata not found")

    return schemas.MetadataResponse(
        id=metadata.id,
        title=metadata.title,
        description=metadata.description,
        director=metadata.director,
    )
