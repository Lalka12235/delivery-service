import uuid
from dataclasses import dataclass
from typing import NewType

from app.domain.entity import IngredientEntity


DishID = NewType('DishID',uuid.UUID)

@dataclass(slots=True, frozen=True)
class DishEntity:
    id: DishID
    restaurant_id: uuid.UUID
    title: str
    price: int
    description: str
    ingredients: list[IngredientEntity]