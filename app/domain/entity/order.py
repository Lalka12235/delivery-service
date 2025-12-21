import uuid
from dataclasses import dataclass
from app.domain.entity import OrderItemEntity
from app.domain.enum import OrderStatus
from datetime import datetime

@dataclass(slots=True,frozen=True)
class OrderEntity:
    id: uuid.UUID
    description: str
    cost: int
    address_id: str
    order_item: list[OrderItemEntity]
    status: OrderStatus
    delivery_time: datetime
    created_at: datetime
    updated_at: datetime
    restaurant_id: uuid.UUID | None
    shop_id: uuid.UUID | None
    courier_id: uuid.UUID | None
    user_id: uuid.UUID