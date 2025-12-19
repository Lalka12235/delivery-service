import uuid
from dataclasses import dataclass


@dataclass(slots=True,frozen=True)
class RestaurantEntity:
    id: uuid.UUID
    title: str
    description: str
    rating: float
    address_id: uuid.UUID