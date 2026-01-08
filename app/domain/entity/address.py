import uuid
from dataclasses import dataclass
from typing import NewType

from app.domain.entity.restaurant import RestaurantID
from app.domain.entity.user import UserID

AddressID = NewType('AddressID',uuid.UUID)

@dataclass(slots=True)
class Coordinates:
    lat: float
    lng: float

@dataclass(slots=True)
class AddressEntity:
    id: AddressID
    city: str
    street: str
    house_number: str
    apartment_number: str
    floor: int
    cords: Coordinates
    user_id: UserID | None
    restaurant_id: RestaurantID | None