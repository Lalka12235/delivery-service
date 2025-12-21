import uuid
from dataclasses import dataclass
from typing import NewType

AddressID = NewType('AddressID',uuid.UUID)

@dataclass(slots=True,frozen=True)
class AddressEntity:
    id: AddressID
    city: str
    street: str
    house_number: str
    apartment_number: str
    floor: int
    user_id: uuid.UUID | None
    restaurant_id: uuid.UUID | None