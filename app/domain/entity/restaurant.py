import uuid
from dataclasses import dataclass
from typing import NewType

from app.domain.entity.address import AddressID

RestaurantID = NewType('RestaurantID',uuid.UUID)

@dataclass(slots=True)
class RestaurantEntity:
    id: RestaurantID
    title: str
    description: str
    start_working_time: str
    end_working_time: str
    rating: float
    address_id: AddressID