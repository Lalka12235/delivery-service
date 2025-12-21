import uuid
from dataclasses import dataclass


@dataclass(slots=True,frozen=True)
class AddressEntity:
    id: uuid.UUID
    city: str
    street: str
    house_number: str
    apartment_number: str
    floor: int
    user_id: uuid.UUID | None
    restaurant_id: uuid.UUID | None