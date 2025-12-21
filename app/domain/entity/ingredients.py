import uuid
from dataclasses import dataclass
from typing import NewType

IngredientID = NewType('IngredientID',uuid.UUID)

@dataclass(slots=True,frozen=True)
class IngredientEntity:
    id: IngredientID
    title: str
    description: str
    weight: float
    dish_id: uuid.UUID