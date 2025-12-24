import uuid
from dataclasses import dataclass
from typing import NewType

from app.domain.entity.dish import DishID

IngredientID = NewType('IngredientID',uuid.UUID)

@dataclass(slots=True,frozen=True)
class IngredientEntity:
    id: IngredientID
    title: str
    description: str
    weight: float
    dish_id: DishID