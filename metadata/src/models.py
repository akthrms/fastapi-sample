from dataclasses import dataclass


@dataclass
class Metadata:
    id: int
    title: str
    description: str
    director: str
