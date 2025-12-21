import uuid
from dataclasses import dataclass


@dataclass(slots=True,frozen=True)
class ShopEntity:
    id: uuid.UUID
    title: str
    description: str
    rating: float
    address_id: uuid.UUID