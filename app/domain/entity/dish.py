import uuid
from dataclasses import dataclass
from typing import NewType

from app.domain.entity import IngredientEntity
from app.domain.entity.restaurant import RestaurantID

DishID = NewType('DishID',uuid.UUID)

@dataclass(slots=True, frozen=True)
class DishEntity:
    id: DishID
    title: str
    price: int
    description: str
    ingredients: list[IngredientEntity]
    restaurant_id: RestaurantID