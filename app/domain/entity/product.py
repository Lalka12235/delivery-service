import uuid
from dataclasses import dataclass
from typing import NewType

ProductID = NewType('ProductID',uuid.UUID)

@dataclass(slots=True,frozen=True)
class ProductEntity:
    id: ProductID
    title: str
    price: int
    weight: float
    description: str
    shop_id: uuid.UUID