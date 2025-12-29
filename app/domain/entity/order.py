import uuid
from dataclasses import dataclass
from typing import NewType

from app.domain.entity import OrderItemEntity
from app.domain.entity.courier import CourierID
from app.domain.entity.restaurant import RestaurantID
from app.domain.entity.shop import ShopID
from app.domain.entity.user import UserID
from app.domain.enum import OrderStatus
from datetime import datetime

OrderID = NewType('OrderID',uuid.UUID)

@dataclass(slots=True)
class OrderEntity:
    id: OrderID
    description: str
    cost: int
    address_id: str
    order_item: list[OrderItemEntity]
    status: OrderStatus
    delivery_time: datetime
    created_at: datetime
    updated_at: datetime
    restaurant_id: RestaurantID | None
    shop_id: ShopID | None
    courier_id: CourierID | None
    user_id: UserID