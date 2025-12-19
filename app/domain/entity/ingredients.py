import uuid
from dataclasses import dataclass


@dataclass(slots=True,frozen=True)
class IngredientEntity:
    id: uuid.UUID
    title: str
    description: str
    weight: float
    dish_id: uuid.UUID