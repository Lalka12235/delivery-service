import uuid
from dataclasses import dataclass

from app.domain.entity import IngredientEntity


@dataclass(slots=True, frozen=True)
class DishEntity:
    id: uuid.UUID
    restaurant_id: uuid.UUID
    title: str
    price: int
    description: str
    ingredients: list[IngredientEntity]