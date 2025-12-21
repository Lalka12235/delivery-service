import uuid
from dataclasses import dataclass
from typing import NewType

ShopID = NewType('ShopID',uuid.UUID)

@dataclass(slots=True,frozen=True)
class ShopEntity:
    id: ShopID
    title: str
    description: str
    rating: float
    address_id: uuid.UUID