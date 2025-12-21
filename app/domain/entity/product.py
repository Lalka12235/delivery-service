import uuid
from dataclasses import dataclass


@dataclass(slots=True,frozen=True)
class ProductEntity:
    id: uuid.UUID
    title: str
    price: int
    weight: float
    description: str
    shop_id: uuid.UUID