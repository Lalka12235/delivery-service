import uuid
from dataclasses import dataclass
from typing import NewType

from app.domain.entity.dish import DishID
from app.domain.entity.order import OrderID
from app.domain.entity.product import ProductID

OrderItemID = NewType('OrderItemID',uuid.UUID)

@dataclass(slots=True)
class OrderItemEntity:
    id: OrderItemID
    quantity: int
    price_at_purchase: int
    order_id: OrderID
    dish_id: DishID | None
    product_id: ProductID | None