from typing import Optional

import models

in_memory_store = [
    models.Metadata(1, "映画1", "概要1", "監督1"),
    models.Metadata(2, "映画2", "概要2", "監督2"),
    models.Metadata(3, "映画3", "概要3", "監督3"),
    models.Metadata(4, "映画4", "概要4", "監督4"),
    models.Metadata(5, "映画5", "概要5", "監督5"),
]


def get_metadata(id: int) -> Optional[models.Metadata]:
    for metadata in in_memory_store:
        if metadata.id == id:
            return metadata

    return None


def get_all() -> list[models.Metadata]:
    return in_memory_store
