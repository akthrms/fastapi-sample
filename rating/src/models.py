from dataclasses import dataclass


@dataclass
class Rating:
    id: int
    metadata_id: int
    value: int
