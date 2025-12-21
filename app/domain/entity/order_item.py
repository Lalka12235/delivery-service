import uuid
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class OrderItemEntity:
    id: uuid.UUID
    quantity: int
    price_at_purchase: int
    order_id: uuid.UUID
    dish_id: uuid.UUID | None
    product_id: uuid.UUID | None