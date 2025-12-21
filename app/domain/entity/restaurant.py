import uuid
from dataclasses import dataclass
from typing import NewType

RestaurantID = NewType('RestaurantID',uuid.UUID)

@dataclass(slots=True,frozen=True)
class RestaurantEntity:
    id: RestaurantID
    title: str
    description: str
    rating: float
    address_id: uuid.UUID