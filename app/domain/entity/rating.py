import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True,frozen=True)
class RatingEntity:
    id: uuid.UUID
    description: str
    rating: float
    user_id: uuid.UUID
    order_id: uuid.UUID
    courier_id: uuid.UUID
    created_at: datetime
    updated_at: datetime