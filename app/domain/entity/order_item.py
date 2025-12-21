import uuid
from dataclasses import dataclass
from typing import NewType

OrderItemID = NewType('OrderItemID',uuid.UUID)

@dataclass(slots=True, frozen=True)
class OrderItemEntity:
    id: OrderItemID
    quantity: int
    price_at_purchase: int
    order_id: uuid.UUID
    dish_id: uuid.UUID | None
    product_id: uuid.UUID | None