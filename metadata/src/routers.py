import cruds
import schemas
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/metadata/{id}", response_model=schemas.MetadataResponse)
def get_metadata_by_id(id: int) -> schemas.MetadataResponse:
    metadata = cruds.get_metadata_by_id(id)
    if metadata is None:
        raise HTTPException(404, "metadata not found")

    return schemas.MetadataResponse(
        id=metadata.id,
        title=metadata.title,
        description=metadata.description,
        director=metadata.director,
    )


@router.get("/metadata", response_model=list[schemas.MetadataResponse])
def get_metadata() -> list[schemas.MetadataResponse]:
    metadata = cruds.get_metadata()
    return [
        schemas.MetadataResponse(
            id=item.id,
            title=item.title,
            description=item.description,
            director=item.director,
        )
        for item in metadata
    ]
