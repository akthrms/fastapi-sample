import cruds
import schemas
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/metadata/{id}", response_model=schemas.GetMetadataResponse)
def get_metadata(id: int) -> schemas.GetMetadataResponse:
    metadata = cruds.get_metadata(id)
    if metadata is None:
        raise HTTPException(404, "metadata not found")

    return schemas.GetMetadataResponse(
        id=metadata.id,
        title=metadata.title,
        description=metadata.description,
        director=metadata.director,
    )


@router.get("/metadata", response_model=list[schemas.GetMetadataResponse])
def get_all() -> list[schemas.GetMetadataResponse]:
    metadata = cruds.get_all()
    return [
        schemas.GetMetadataResponse(
            id=item.id,
            title=item.title,
            description=item.description,
            director=item.director,
        )
        for item in metadata
    ]
