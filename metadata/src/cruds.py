from typing import Optional

import models

in_memory_store = {
    1: models.Metadata(1, "映画1", "概要1", "監督1"),
    2: models.Metadata(2, "映画2", "概要2", "監督2"),
    3: models.Metadata(3, "映画3", "概要3", "監督3"),
    4: models.Metadata(4, "映画4", "概要4", "監督4"),
    5: models.Metadata(5, "映画5", "概要5", "監督5"),
}


def get_metadata(id: int) -> Optional[models.Metadata]:
    for key, metadata in in_memory_store.items():
        if key == id:
            return metadata

    return None
