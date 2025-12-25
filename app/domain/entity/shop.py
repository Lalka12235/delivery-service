import uuid
from dataclasses import dataclass
from typing import NewType

from app.domain.entity.address import AddressID

ShopID = NewType('ShopID',uuid.UUID)

@dataclass(slots=True)
class ShopEntity:
    id: ShopID
    title: str
    description: str
    rating: float
    address_id: AddressID