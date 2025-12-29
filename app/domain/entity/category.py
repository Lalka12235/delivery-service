import uuid
from dataclasses import dataclass
from typing import NewType

CategoryID = NewType('CategoryID',uuid.UUID)

@dataclass(slots=True)
class CategoryEntity:
    id: CategoryID
    title: str
    description: str | None
    adult: bool