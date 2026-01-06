import uuid
from dataclasses import dataclass
from typing import NewType

from app.domain.entity import IngredientEntity
from app.domain.entity.category import CategoryID
from app.domain.entity.restaurant import RestaurantID

DishID = NewType('DishID',uuid.UUID)

@dataclass(slots=True)
class DishEntity:
    id: DishID
    title: str
    price: int
    description: str
    ingredients: list[IngredientEntity]
    is_active: bool
    restaurant_id: RestaurantID
    category_id: CategoryID