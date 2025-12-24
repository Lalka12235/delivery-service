import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import NewType

from app.domain.entity.courier import CourierID
from app.domain.entity.order import OrderID
from app.domain.entity.user import UserID

ReviewID = NewType('ReviewID',uuid.UUID)

@dataclass(slots=True,frozen=True)
class ReviewEntity:
    id: ReviewID
    title: str
    description: str
    rating: float
    user_id: UserID
    order_id: OrderID
    courier_id: CourierID
    created_at: datetime
    updated_at: datetime